#!/usr/bin/env python3
"""Source-provenance-aware, unattended Botanical Atlas GitHub publisher."""
import argparse, base64, copy, datetime, json, os, re, shutil, sqlite3, sys, tempfile
from pathlib import Path
from urllib.parse import urlsplit

ROOT=Path(__file__).resolve().parents[1]
COLLS=('organisms','compounds','occurrences','domain_notes','safety','cultural_uses','sources','structures','binding','practice_claims','dose_guidance','folklore','regulatory_status','bioactivities','medical_systems','medicinal_materials','formulas','formula_components','interaction_evidence')
IDS={'organisms':'id','compounds':'id','occurrences':'id','cultural_uses':'id','sources':'id','structures':'compound_id','binding':'id','practice_claims':'id','dose_guidance':'id','folklore':'id','regulatory_status':'id','bioactivities':'id','medical_systems':'id','medicinal_materials':'id','formulas':'id','formula_components':'id','interaction_evidence':'id'}
IDENTITY={'organisms':('scientific_name',),'compounds':('display_name',),'sources':('url',),'occurrences':('organism_id','compound_id'),'cultural_uses':('organism_id',),'structures':('compound_id',),'binding':('compound_id',),'practice_claims':('organism_id',),'dose_guidance':('organism_id',),'folklore':('organism_id',),'regulatory_status':('organism_id',),'bioactivities':('agent_type','compound_id','organism_id','target_taxon','life_stage','endpoint'),'medical_systems':('name',),'medicinal_materials':('organism_id','part','preparation','processing'),'formulas':('original_term','system_id'),'formula_components':('formula_id','material_id'),'interaction_evidence':('left_ref','right_ref','interaction_type','evidence_tier')}
def die(message): raise ValueError(message)
def get(path):
    obj=json.loads(path.read_text('utf-8'))
    if not isinstance(obj,dict):die('Expected JSON object: '+str(path))
    return obj
def goodurl(url):
    if not isinstance(url,str):return False
    p=urlsplit(url)
    return p.scheme=='https' and bool(p.hostname) and not p.username and not p.password
def check(data):
    for key in COLLS:
        rows=data.get(key)
        if not isinstance(rows,list) or any(not isinstance(x,dict) for x in rows):die('Invalid collection: '+key)
        k=IDS.get(key)
        if k:
            names=[row.get(k) for row in rows]
            if any(not isinstance(v,str) or not v for v in names) or len(names)!=len(set(names)):die('Missing or duplicate ID: '+key)
    org={row['id'] for row in data['organisms']}
    cmp={row['id'] for row in data['compounds']}
    sources={row['id'] for row in data['sources']}
    for row in data['organisms']:
        if not row.get('scientific_name') or not row.get('common_name'):die('Incomplete taxon')
    for row in data['compounds']:
        if not row.get('display_name') or not row.get('entity_type'):die('Incomplete chemical identity')
    for key in ('occurrences','domain_notes','safety','cultural_uses','practice_claims','dose_guidance','folklore','regulatory_status'):
        for row in data[key]:
            if row.get('organism_id') not in org:die('Unknown organism in '+key)
    for row in data['occurrences']+data['structures']+data['binding']:
        if row.get('compound_id') not in cmp:die('Unknown compound')
    for row in data['occurrences']+data['cultural_uses']:
        if row.get('source_id') and row['source_id'] not in sources:die('Unknown source')
    for row in data['cultural_uses']:
        if not all(row.get(k) for k in ('region','tradition','part','preparation','reported_use','claim_kind','source_id','limitations')):die('Unattributed cultural claim')
        if row.get('clinical_efficacy_established') is True and row.get('claim_kind')!='clinical_evidence':die('Traditional claim mislabeled clinical')
    # Each independently sourced medical/cultural lens must belong to a real organism and existing source.
    for key in ('practice_claims','dose_guidance','folklore','regulatory_status'):
        for row in data[key]:
            if row.get('source_id') not in sources:die('Unknown evidence source in '+key)
            if not row.get('id'):die('Missing ID in '+key)
    for row in data['practice_claims']:
        if not all(row.get(k) for k in ('system','tradition','region','condition_or_goal','plant_part','preparation','evidence_tier','claim_type','limitations')):die('Incomplete practice claim')
        if row.get('clinical_efficacy_established') is True and row.get('claim_type') not in ('clinical_evidence','well_established_monograph'):die('Nonclinical practice falsely declared proven')
    for row in data['dose_guidance']:
        if not all(row.get(k) for k in ('part','preparation','route','population','amount_text','intended_use','evidence_status','upper_limit_status','risks','contraindications')):die('Incomplete dosage context')
        if row.get('guaranteed_safe') is True:die('Universal guaranteed safety is not a supported dosage claim')
        if row.get('evidence_status')=='not_established_across_products' and any(ch.isdigit() for ch in row['amount_text']):die('Speculative numeric dose')
    for row in data['folklore']:
        if not all(row.get(k) for k in ('tradition','region','theme','description','claim_type','evidence_tier','limitations')):die('Incomplete folklore context')
        if row.get('clinical_claim') is True or row.get('public_knowledge') is not True:die('Folklore must be public and nonclinical')
    for row in data['regulatory_status']:
        if not all(row.get(k) for k in ('jurisdiction','regulator','category','preparation_scope','status_text','date_checked','limitations')):die('Incomplete regulatory status')
    for row in data['bioactivities']:
        if row.get('source_id') not in sources:die('Bioactivity must cite an Atlas source')
        if row.get('compound_id') and row['compound_id'] not in cmp:die('Unknown bioactivity compound')
        if row.get('organism_id') and row['organism_id'] not in org:die('Unknown bioactivity organism')
        if row.get('agent_type')=='isolated_compound' and not row.get('compound_id'):die('Missing tested molecule')
        if row.get('agent_type')=='plant_essential_oil' and not row.get('organism_id'):die('Missing plant oil organism')
        if row.get('evidence_tier') not in ('in_vitro','ex_vivo','animal','human_trial','human_observational','in_silico'):die('Unrecognized study level')
        if not all(row.get(k) for k in ('id','agent_type','activity_category','target_taxon','life_stage','study_model','endpoint','observed_effect','mechanism_status','dose_translation','limitations')):die('Incomplete bioactivity')
        if row.get('human_clinical_efficacy_established') is True and row.get('evidence_tier')!='human_trial':die('Unsupported preclinical cure claim')
        if row.get('evidence_tier')!='human_trial' and row.get('dose_guidance'):die('Experimental concentration misrepresented as treatment dose')
        metric=row.get('metric')
        if metric is not None:
            if not isinstance(metric,dict) or metric.get('name') not in ('IC50','EC50','MIC','ED50','LC50','percent_inhibition','qualitative'):die('Invalid activity metric')
            if not isinstance(metric.get('value'),(int,float)) or isinstance(metric.get('value'),bool) or metric['value']<0:die('Invalid bioactivity assay measurement')
            if not metric.get('unit'):die('Missing laboratory concentration units')
    # Tradition-specific ontologies: don't flatten Qi, mizaj and dosha into one biomedical diagnosis.
    system_ids={x['id'] for x in data['medical_systems']}
    for ms in data['medical_systems']:
        if not ms.get('name') or not goodurl(ms.get('reference_url')):die('Missing medical-system terminology reference')
        if not isinstance(ms.get('axes'),list) or not ms['axes']:die('Medical system has no native concept axes')
        axes=[axis.get('id') for axis in ms['axes'] if isinstance(axis,dict)]
        if len(axes)!=len(ms['axes']) or len(set(axes))!=len(axes) or any(not x for x in axes):die('Invalid medical system axes')
    for claim in data['practice_claims']:
        sid=claim.get('system_id')
        if sid and sid not in system_ids:die('Unknown medical system referenced by practice claim')
        fd=claim.get('framework_details')
        if fd is not None:
            if not isinstance(fd,dict) or any(not isinstance(v,(str,list)) or isinstance(v,list) and (not all(isinstance(q,str) for q in v)) for v in fd.values()):die('Malformed framework details')
            if not sid:die('Native framework fields require canonical system ID')
        if claim.get('profile_depth')=='deep':
            if not (sid and claim.get('original_term') and fd and claim.get('source_id') and claim.get('limitations')):die('Incomplete deep medical-system profile')
            refids=claim.get('supporting_source_ids',[])
            if not isinstance(refids,list) or any(x not in sources for x in refids):die('Unknown supporting framework source')
            if claim.get('clinical_efficacy_established') is True and claim.get('claim_type') not in ('clinical_evidence','well_established_monograph'):die('Traditional deep profile called clinically established')
    # Material identity is distinct from botanical species, extract and isolated constituent.
    msids={r['id'] for r in data['medical_systems']}
    mids={r['id'] for r in data['medicinal_materials']}
    fids={r['id'] for r in data['formulas']}
    refs={'material':mids,'formula':fids,'compound':cmp}
    for m in data['medicinal_materials']:
        if not all(m.get(k) for k in ('id','organism_id','part','preparation','processing','material_class','tradition','source_id','identity_status','limitations')):die('Incomplete medicinal material')
        if m['organism_id'] not in org or m['source_id'] not in sources:die('Unattributed medicinal material')
        if m.get('system_id') and m['system_id'] not in msids:die('Unknown material medical system')
        if m.get('safe_to_ingest') is True:die('Plant material identity alone never establishes safety')
    for formula in data['formulas']:
        if not all(formula.get(k) for k in ('id','name','original_term','system_id','tradition','source_id','claimed_use','claim_type','evidence_tier','limitations')):die('Incomplete formula definition')
        if formula['system_id'] not in msids or formula['source_id'] not in sources:die('Unattributed formula')
        if formula.get('clinical_efficacy_established') is True and formula.get('evidence_tier') not in ('human_trial','systematic_review_of_human_trials'):die('Tradition cannot establish formula clinical efficacy')
        if formula.get('standard_safe_dose') is not None:die('Formula dossier cannot claim universally safe dose')
    linked={}
    for comp in data['formula_components']:
        if not all(comp.get(k) for k in ('id','formula_id','material_id','source_id','role','limitations')):die('Incomplete formula component')
        if comp['formula_id'] not in fids or comp['material_id'] not in mids or comp['source_id'] not in sources:die('Broken formula material or source link')
        linked.setdefault(comp['formula_id'],[]).append(comp['material_id'])
        if comp.get('safe_dose') is not None:die('Formula component cannot set unverified safe intake')
    for formula in data['formulas']:
        members=linked.get(formula['id'],[])
        if len(members)<2 or len(members)!=len(set(members)):die('Multi-herb formula needs at least two distinct authenticated materials')
    for ev in data['interaction_evidence']:
        if not all(ev.get(k) for k in ('id','left_ref','right_ref','interaction_type','evidence_tier','method','observation','source_id','limitations')):die('Incomplete interaction evidence')
        if ev['source_id'] not in sources:die('Unattributed interaction evidence')
        for ref in (ev['left_ref'],ev['right_ref']):
            if not isinstance(ref,str) or ':' not in ref:die('Interaction reference must be typed')
            kind,ident=ref.split(':',1)
            if kind not in refs or ident not in refs[kind]:die('Unknown interaction entity')
        if ev['left_ref']==ev['right_ref']:die('Interaction cannot self-reference')
        if ev.get('clinical_efficacy_established') is True and ev.get('evidence_tier') not in ('human_trial','systematic_review_of_human_trials'):die('Interaction hypothesis falsely described as proven efficacy')
        if ev['interaction_type'] in ('laboratory_synergy','laboratory_antagonism') and not ev.get('assay_endpoint'):die('Synergy/antagonism require explicit experimental assay endpoint')
    for row in data['practice_claims']+data['dose_guidance']:
        if row.get('material_id') and row['material_id'] not in mids:die('Practice or dose refers to missing medicinal material')
    return True
def verify(batch):
    ident=batch.get('batch_id','')
    if not isinstance(ident,str) or not re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9_.-]{5,100}',ident):die('Invalid batch ID')
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',str(batch.get('research_date',''))):die('Invalid research date')
    if not goodurl(batch.get('research_reference_url')):die('Missing HTTPS research reference')
    if set(batch)-set(COLLS)-{'batch_id','research_date','research_reference_url','summary','research_method'}:die('Unexpected batch fields')
    if not any(batch.get(k) for k in COLLS):die('Empty batch')
    for key in COLLS:
        if key in batch and (not isinstance(batch[key],list) or any(not isinstance(x,dict) for x in batch[key])):die('Invalid batch array '+key)
    for row in batch.get('sources',[]):
        if not all(row.get(k) for k in ('id','title','organization','url')) or not goodurl(row['url']):die('Unattributed source')
    for row in batch.get('occurrences',[]):
        if not row.get('source_id') or not row.get('verification'):die('Uncited or ungraded chemistry occurrence')
    for row in batch.get('cultural_uses',[]):
        if not row.get('source_id') or not row.get('verification') or row.get('clinical_efficacy_established') is True:die('Invalid cultural evidence')
    for row in batch.get('structures',[]):
        if row.get('smiles') and not goodurl(row.get('source_url')):die('SMILES without verifiable chemical source')
        f=row.get('structure_file')
        if f and (f.startswith('/') or '..' in Path(f).parts or not (ROOT/'assets'/f).is_file()):die('Missing or invalid local molecule asset')
    for row in batch.get('binding',[]):
        if not row.get('evidence_tier') or not row.get('method') or not row.get('source_refs') or not all(goodurl(x) for x in row['source_refs']):die('Unattributed target binding')
    for key in ('domain_notes','safety'):
        if any(not row.get('quality') for row in batch.get(key,[])):die('Ungraded '+key)
    for key in ('practice_claims','dose_guidance','folklore','regulatory_status'):
        for row in batch.get(key,[]):
            if not row.get('source_id'):die('Uncited '+key)
    for row in batch.get('practice_claims',[]):
        if not row.get('evidence_tier') or not row.get('limitations'):die('Ungraded medical-system claim')
    for row in batch.get('dose_guidance',[]):
        if not row.get('evidence_status') or not row.get('population') or not row.get('preparation') or row.get('guaranteed_safe') is True:die('Unsafe or incomplete dose claim')
    for row in batch.get('folklore',[]):
        if row.get('public_knowledge') is not True or row.get('clinical_claim') is True:die('Restricted or medicalized folklore')
    for row in batch.get('bioactivities',[]):
        if not all(row.get(k) for k in ('id','source_id','agent_type','target_taxon','life_stage','study_model','evidence_tier','endpoint','observed_effect','limitations','dose_translation')):die('Incomplete sourced bioactivity batch')
        if row.get('human_clinical_efficacy_established') is True and row.get('evidence_tier')!='human_trial':die('Preclinical assay is not proven clinical treatment')

    for ms in batch.get('medical_systems',[]):
        if not ms.get('name') or not goodurl(ms.get('reference_url')) or not isinstance(ms.get('axes'),list):die('Invalid medical-system registry entry')
    for row in batch.get('practice_claims',[]):
        if row.get('profile_depth')=='deep' and not (row.get('system_id') and row.get('original_term') and isinstance(row.get('framework_details'),dict) and row.get('framework_details')):die('Incomplete deep medical profile')
    for key in ('medicinal_materials','formulas','formula_components','interaction_evidence'):
        for row in batch.get(key,[]):
            if not row.get('id') or not row.get('source_id'):die('Unattributed formula/material batch record')
    for item in batch.get('formulas',[]):
        if not item.get('limitations') or not item.get('evidence_tier'):die('Formula missing evidence limits')
    for row in batch.get('interaction_evidence',[]):
        if not row.get('evidence_tier') or not row.get('method') or not row.get('limitations'):die('Unsupported interaction assertion')
def merge(data,batch):
    result=copy.deepcopy(data)
    for coll in COLLS:
        rows=result[coll];new=batch.get(coll,[]);k=IDS.get(coll)
        if k:
            ix={row[k]:i for i,row in enumerate(rows)}
            for row in new:
                ident=row.get(k)
                if not isinstance(ident,str) or not ident:die('Missing ID in '+coll)
                if ident in ix:
                    prior=rows[ix[ident]]
                    for field in IDENTITY.get(coll,()):
                        if field in row and field in prior and row[field]!=prior[field]:die('Identity conflict: '+coll+'/'+ident)
                    rows[ix[ident]]={**prior,**row}
                else:
                    ix[ident]=len(rows);rows.append(row)
        else:
            old={json.dumps(r,sort_keys=True) for r in rows}
            for row in new:
                stamp=json.dumps(row,sort_keys=True)
                if stamp not in old:rows.append(row);old.add(stamp)
    check(result)
    return result
def save(path,blob):
    path.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent,delete=False) as f:
        f.write(blob);tmp=f.name
    os.replace(tmp,path)
def render(data):
    enriched=copy.deepcopy(data);art={}
    for item in data['structures']:
        fname=item.get('structure_file')
        if not fname:continue
        f=(ROOT/'assets'/fname)
        if f.is_file() and f.resolve().is_relative_to((ROOT/'assets').resolve()):
            raw=f.read_bytes()
            if len(raw)>200000 or any(x in raw.lower() for x in (b'<script',b'onload=',b'javascript:')):die('Unsafe molecule drawing')
            art[item['compound_id']]='data:image/svg+xml;base64,'+base64.b64encode(raw).decode('ascii')
    enriched['structure_assets']=art
    token='__EMBED_JSON__'
    template=(ROOT/'app/template.html').read_text('utf-8')
    if template.count(token)!=1:die('Template placeholder invalid')
    safe=json.dumps(enriched,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
    html=template.replace(token,safe)
    for marker,path in (('__WB_JS__',ROOT/'app/workbench.js'),('__WB_CSS__',ROOT/'app/workbench.css')):
        if html.count(marker)!=1:die('Workbench template placeholder missing: '+marker)
        asset=path.read_text('utf-8')
        if not asset or '</script' in asset.lower() or '</style' in asset.lower():die('Untrusted workbench asset content')
        html=html.replace(marker,asset)
    return html.encode('utf-8')
def coverage_report(data):
    """Deterministic editorial coverage metrics: not medical evidence and not a link-availability scan."""
    ids=lambda key,ref='organism_id':{r[ref] for r in data[key] if r.get(ref)}
    attributed={r['id'] for r in data['sources'] if goodurl(r.get('url'))}
    constituents={r['compound_id'] for r in data['bioactivities'] if r.get('compound_id')}
    hard_to_verify=[r['id'] for r in data['sources'] if not goodurl(r.get('url'))]
    weaker_occurrences=[r.get('id') for r in data['occurrences'] if 'legacy' in str(r.get('verification','')).lower() or r.get('source_id') not in attributed]
    species={r['id'] for r in data['organisms']}
    material_covered=ids('medicinal_materials')
    medical=ids('practice_claims')
    return {
        'schema':'atlas_editorial_coverage_v1',
        'catalog_revision':data['meta'].get('catalog_revision'),
        'warning':'Coverage means a record exists, not verified efficacy, clinical benefit or safe dosing. Source URLs have not been independently fetched.',
        'counts':{key:len(data[key]) for key in COLLS},
        'plant_count':sum(1 for r in data['organisms'] if r.get('kingdom')=='Plantae'),
        'fungus_count':sum(1 for r in data['organisms'] if r.get('kingdom')=='Fungi'),
        'organisms_with_claims':len(medical),
        'organisms_without_claims':len(species-medical),
        'organisms_with_authenticated_material_records':len(material_covered),
        'organisms_without_material_records':len(species-material_covered),
        'organisms_with_dose_context':len(ids('dose_guidance')),
        'organisms_with_folklore':len(ids('folklore')),
        'deep_medicinal_profiles':sum(1 for r in data['practice_claims'] if r.get('profile_depth')=='deep'),
        'compound_identities_with_assay_records':len(constituents),
        'compound_identities_without_assay_records':len(data['compounds'])-len(constituents),
        'legacy_or_unclear_chemical_occurrence_ids':sorted(x for x in weaker_occurrences if x),
        'source_entries_missing_usable_url':sorted(hard_to_verify),
        'unreviewed_assays_are_not_zero_effects':True
    }
def dbwrite(data,path):
    cx=sqlite3.connect(path)
    try:
        cx.executescript('CREATE TABLE objects(category TEXT,id TEXT,json TEXT,PRIMARY KEY(category,id));CREATE TABLE relations(category TEXT,id TEXT,organism_id TEXT,compound_id TEXT,source_id TEXT);CREATE INDEX rel_org ON relations(organism_id);CREATE INDEX rel_comp ON relations(compound_id);')
        for coll in COLLS:
            key=IDS.get(coll)
            for i,row in enumerate(data[coll]):
                rid=row.get(key) if key else coll+'-'+str(i)
                cx.execute('INSERT INTO objects VALUES(?,?,?)',(coll,rid,json.dumps(row,ensure_ascii=False)))
                cx.execute('INSERT INTO relations VALUES(?,?,?,?,?)',(coll,rid,row.get('organism_id'),row.get('compound_id'),row.get('source_id')))
        if cx.execute('PRAGMA integrity_check').fetchone()[0]!='ok':die('SQLite validation failed')
        cx.commit()
    finally:cx.close()
def run(ingest=False):
    canonical=ROOT/'data/atlas.json';state=get(canonical);check(state)
    batches=sorted((ROOT/'incoming').glob('*.json')) if ingest else []
    seen=set()
    for file in batches:
        batch=get(file);verify(batch)
        if batch['batch_id']!=file.stem or batch['batch_id'] in seen or (ROOT/'processed'/file.name).exists():die('Duplicate/replayed or misnamed batch')
        seen.add(batch['batch_id'])
        state=merge(state,batch)
    if batches:
        state['meta']['catalog_revision']=int(state['meta'].get('catalog_revision',0))+len(batches)
        state['meta']['last_ingestion_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    check(state);html=render(state)
    with tempfile.TemporaryDirectory() as tmp:
        sql=Path(tmp)/'atlas.sqlite';dbwrite(state,sql)
        sqlite_blob=sql.read_bytes()
    if batches:save(canonical,(json.dumps(state,indent=2,ensure_ascii=False)+'\n').encode('utf-8'))
    save(ROOT/'site/index.html',html)
    save(ROOT/'data/atlas.sqlite',sqlite_blob)
    save(ROOT/'data/coverage.json',(json.dumps(coverage_report(state),indent=2,ensure_ascii=False)+'\n').encode('utf-8'))
    for file in batches:
        (ROOT/'processed').mkdir(exist_ok=True)
        shutil.move(str(file),str(ROOT/'processed'/file.name))
    print(json.dumps({'published_batches':len(batches),'organisms':len(state['organisms']),'compounds':len(state['compounds']),'cultural_uses':len(state['cultural_uses'])}))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('command',choices=('validate','build','ingest'));a=p.parse_args()
    try:
        if a.command=='validate':
            check(get(ROOT/'data/atlas.json'));print('PASS: Atlas integrity')
        else:run(a.command=='ingest')
    except (ValueError,KeyError,TypeError,sqlite3.Error,json.JSONDecodeError) as e:
        print('FAIL:',e,file=sys.stderr);sys.exit(1)
