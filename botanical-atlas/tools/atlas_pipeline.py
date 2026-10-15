#!/usr/bin/env python3
"""Source-provenance-aware, unattended Botanical Atlas GitHub publisher."""
import argparse, base64, copy, datetime, json, os, re, shutil, sqlite3, sys, tempfile
from pathlib import Path
from urllib.parse import urlsplit

ROOT=Path(__file__).resolve().parents[1]
COLLS=('organisms','compounds','occurrences','domain_notes','safety','cultural_uses','sources','structures','binding')
IDS={'organisms':'id','compounds':'id','occurrences':'id','cultural_uses':'id','sources':'id','structures':'compound_id','binding':'id'}
IDENTITY={'organisms':('scientific_name',),'compounds':('display_name',),'sources':('url',),'occurrences':('organism_id','compound_id'),'cultural_uses':('organism_id',),'structures':('compound_id',),'binding':('compound_id',)}
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
    for key in ('occurrences','domain_notes','safety','cultural_uses'):
        for row in data[key]:
            if row.get('organism_id') not in org:die('Unknown organism in '+key)
    for row in data['occurrences']+data['structures']+data['binding']:
        if row.get('compound_id') not in cmp:die('Unknown compound')
    for row in data['occurrences']+data['cultural_uses']:
        if row.get('source_id') and row['source_id'] not in sources:die('Unknown source')
    for row in data['cultural_uses']:
        if not all(row.get(k) for k in ('region','tradition','part','preparation','reported_use','claim_kind','source_id','limitations')):die('Unattributed cultural claim')
        if row.get('clinical_efficacy_established') is True and row.get('claim_kind')!='clinical_evidence':die('Traditional claim mislabeled clinical')
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
    return template.replace(token,safe).encode('utf-8')
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
