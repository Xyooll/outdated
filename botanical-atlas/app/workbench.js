(function workbench(){
  'use strict';
  const holder=document.getElementById('workbench-shell');
  const toggle=document.getElementById('workbench-toggle');
  const catalog=document.querySelector('.layout');
  if(!holder||!toggle||!catalog)return;
  let db;
  try{db=JSON.parse(document.getElementById('atlas-data').textContent)}catch(err){return;}
  const organisms=db.organisms||[],compounds=db.compounds||[],occurrences=db.occurrences||[],cultures=db.cultural_uses||[];
  const medicine=db.practice_claims||[],doses=db.dose_guidance||[],folklore=db.folklore||[],safety=db.safety||[],structures=db.structures||[],materials=db.medicinal_materials||[],formulas=db.formulas||[],formulaParts=db.formula_components||[];
  const sourceMap=new Map((db.sources||[]).map(s=>[s.id,s])),compoundMap=new Map(compounds.map(c=>[c.id,c]));
  const names=new Map(organisms.map(o=>[o.id,o]));
  const occByOrg=new Map(organisms.map(o=>[o.id,[]]));
  for(const x of occurrences){if(occByOrg.has(x.organism_id))occByOrg.get(x.organism_id).push(x);}
  const escapeHtml=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const esc=escapeHtml;
  const linked=(id)=>{const s=sourceMap.get(id);return s&&/^https:\/\//i.test(s.url||'')?`<a href="${esc(s.url)}" target="_blank" rel="noopener noreferrer">${esc(s.organization||s.title||'Source')} ↗</a>`:'<span class="wb-warning">Citation unresolved</span>';};
  const entries=(collection,id)=>collection.filter(r=>r.organism_id===id);
  function credibleOccurrence(x){
    const verification=String(x.verification||'').toLowerCase();
    return !!x.source_id&&sourceMap.has(x.source_id)&&!!verification&&!/legacy|unreviewed|unverified|pending|missing/.test(verification);
  }
  function coverage(o){
    const id=o.id,os=occByOrg.get(id)||[];
    const checkedStructures=os.some(x=>structures.some(s=>s.compound_id===x.compound_id&&(s.source_url||s.pubchem_cid)&&!/(pending|unverified)/i.test(s.review_status||s.status||'')));
    const axes={
      'Attributed uses':entries(cultures,id).some(x=>!!sourceMap.get(x.source_id)),
      'Medical perspectives':entries(medicine,id).some(x=>!!sourceMap.get(x.source_id)),
      'Dose context':entries(doses,id).some(x=>!!sourceMap.get(x.source_id)),
      'Safety information':entries(safety,id).length>0,
      'Folklore':entries(folklore,id).some(x=>!!sourceMap.get(x.source_id)),
      'Structure link':checkedStructures,
      'Identified preparation':entries(materials,id).some(x=>!!sourceMap.get(x.source_id)),
      'Linked formula':formulaParts.some(p=>materials.some(m=>m.id===p.material_id&&m.organism_id===id))
    };
    return {axes,score:Object.values(axes).filter(Boolean).length};
  }
  let active=false,tab='overview',filter='',sort='least',focus='BOT-004',selected=['BOT-004','BOT-007',''],verifiedOnly=false;
  function show(){
    active=true;holder.hidden=false;catalog.hidden=true;toggle.classList.add('on');toggle.setAttribute('aria-pressed','true');render();
    holder.scrollIntoView({block:'start',behavior:'smooth'});
  }
  function hide(){active=false;holder.hidden=true;catalog.hidden=false;toggle.classList.remove('on');toggle.setAttribute('aria-pressed','false');}
  toggle.addEventListener('click',()=>active?hide():show());
  for(const nav of document.querySelectorAll('[data-mode]'))nav.addEventListener('click',hide);
  const options=(id,empty=false)=>`${empty?'<option value="">No third plant</option>':''}${organisms.map(o=>`<option value="${esc(o.id)}" ${id===o.id?'selected':''}>${esc(o.common_name)} (${esc(o.scientific_name)})</option>`).join('')}`;
  const card=(title,content,meta='')=>`<article class="wb-tile"><h3>${esc(title)}</h3>${meta?`<div class="wb-meta">${esc(meta)}</div>`:''}${content}</article>`;
  const small=(str)=>`<div class="wb-muted">${esc(str)}</div>`;
  const flags=(rows)=>rows.length?rows.map(r=>`<div class="wb-entry">${esc(r.alert||r.risks||'Risk summary pending')}<div class="wb-meta">${esc(r.quality||r.evidence_status||'Unspecified quality')}</div>${r.source_id?linked(r.source_id):'<span class="wb-warning">Source not attached to this safety note</span>'}</div>`).join(''):small('No recorded safety assessment. This does not establish safety.');
  function overview(){
    const tally=organisms.map(o=>({o,...coverage(o)})).filter(r=>[r.o.common_name,r.o.scientific_name,r.o.geographic_context,...entries(medicine,r.o.id).map(x=>x.condition_or_goal+' '+x.system)].some(x=>String(x||'').toLowerCase().includes(filter.toLowerCase())));
    tally.sort((a,b)=>sort==='most'?b.score-a.score||a.o.common_name.localeCompare(b.o.common_name):sort==='name'?a.o.common_name.localeCompare(b.o.common_name):a.score-b.score||a.o.common_name.localeCompare(b.o.common_name));
    const hasMedicine=organisms.filter(o=>entries(medicine,o.id).some(r=>sourceMap.has(r.source_id))).length,hasDose=organisms.filter(o=>entries(doses,o.id).length).length,hasFolklore=organisms.filter(o=>entries(folklore,o.id).length).length;
    return `<div class="wb-stats"><div><strong>${organisms.length}</strong><span>Cataloged organisms</span></div><div><strong>${hasMedicine}</strong><span>With sourced medical perspectives</span></div><div><strong>${hasDose}</strong><span>With dose context</span></div><div><strong>${hasFolklore}</strong><span>With folklore records</span></div></div>
    <div class="wb-note">Preparation and formula identity are independently counted. The Atlas currently contains ${materials.length} recorded materials and ${formulas.length} documented multi-ingredient formulas. Chemical overlaps do not prove synergy.</div>
    <div class="wb-note">Coverage shows what has been <strong>documented in the Atlas</strong>, not how effective, safe or comprehensive an organism is. Blank fields mean research remains to be done.</div>
    <div class="wb-controls"><label>Search catalog or indication<input id="wb-filter" class="wb-input" value="${esc(filter)}" placeholder="e.g. nausea, clove, sleep"></label><label>Order<select id="wb-sort" class="wb-input"><option value="least" ${sort==='least'?'selected':''}>Most research needed</option><option value="most" ${sort==='most'?'selected':''}>Most documented</option><option value="name" ${sort==='name'?'selected':''}>Name A–Z</option></select></label></div>
    <div class="wb-coverage-list">${tally.map(({o,axes,score})=>`<article class="wb-coverage-row"><div><button class="wb-link" data-open="${esc(o.id)}">${esc(o.common_name)} ↗</button><div class="wb-meta"><em>${esc(o.scientific_name)}</em></div></div><span class="wb-progress">${score}/8 documented</span><div class="wb-statuses">${Object.entries(axes).map(([k,v])=>`<span class="wb-flag ${v?'wb-yes':'wb-no'}" title="${esc(k)}">${v?'✓':'○'} ${esc(k)}</span>`).join('')}</div></article>`).join('')||'<p>No matching identities</p>'}</div>`;
  }
  function compare(){
    const ids=[...new Set(selected.filter(id=>names.has(id)))],rows=ids.map(id=>names.get(id));if(!rows.length)return small('Choose a plant to compare.');
    const overlap=new Map();for(const id of ids){for(const r of occByOrg.get(id)||[]){const c=compoundMap.get(r.compound_id);if(c){const m=overlap.get(c.id)||{name:c.display_name,ids:new Set(),evidence:0,total:0};m.ids.add(id);m.total++;if(credibleOccurrence(r))m.evidence++;overlap.set(c.id,m);}}}
    const shared=[...overlap.values()].filter(v=>v.ids.size>=2).sort((a,b)=>a.name.localeCompare(b.name));
    return `<div class="wb-controls">${selected.map((id,i)=>`<label>${i===0?'First plant':i===1?'Second plant':'Optional third plant'}<select class="wb-input" data-select-compare="${i}">${options(id,i===2)}</select></label>`).join('')}</div>
    <div class="wb-note">Comparisons distinguish <strong>documented uses</strong>, clinical observations, traditional frameworks and hypotheses. A shared chemical name does not prove comparable concentration, absorption, efficacy or synergy.</div>
    <div class="wb-compare">${rows.map(o=>{const id=o.id,med=entries(medicine,id),dd=entries(doses,id),ss=entries(safety,id),cc=entries(cultures,id),ff=entries(folklore,id),os=occByOrg.get(id)||[];return `<article class="wb-column"><div class="wb-column-head"><button class="wb-link" data-open="${esc(id)}">${esc(o.common_name)} ↗</button><div><em>${esc(o.scientific_name)}</em></div></div>
    ${card('Plant part / preparations',small(o.part_and_preparation_note||'Not documented'))}
    ${card('Known medicinal materials',entries(materials,id).length?entries(materials,id).map(m=>`<div class="wb-entry"><b>${esc(m.part)}</b><div class="wb-meta">${esc(m.preparation)} · ${esc(m.processing)}</div><p>${esc(m.limitations)}</p>${linked(m.source_id)}</div>`).join(''):small('No preparation-specific material authentication research yet.'))}
    ${card('Linked traditional formulas',formulaParts.filter(x=>materials.some(m=>m.id===x.material_id&&m.organism_id===id)).length?formulaParts.filter(x=>materials.some(m=>m.id===x.material_id&&m.organism_id===id)).map(x=>{let f=formulas.find(y=>y.id===x.formula_id);return `<div class="wb-entry"><b>${esc(f?.name||x.formula_id)}</b><div class="wb-meta">${esc(f?.evidence_tier||'Unknown')}</div><p>Historical composition is not proof of efficacy or safety.</p>${linked(x.source_id)}</div>`}).join(''):small('No authenticated multi-herb formula link yet.'))}
    ${card('Medicinal evidence',med.length?med.map(x=>`<div class="wb-entry"><strong>${esc(x.condition_or_goal)}</strong><div class="wb-meta">${esc(x.system)} · ${esc(x.evidence_tier)}</div><p>${esc(x.preparation)}</p>${linked(x.source_id)}</div>`).join(''):small('No independently sourced medicinal perspective yet.'))}
    ${card('Doses & formulation',dd.length?dd.map(x=>`<div class="wb-entry"><strong>${esc(x.amount_text)}</strong><div class="wb-meta">${esc(x.part)} · ${esc(x.preparation)} · ${esc(x.population)} · ${esc(x.evidence_status)}</div><p>${esc(x.risks)}</p>${linked(x.source_id)}</div>`).join(''):small('Safe dose not established in Atlas.'))}
    ${card('Safety',flags(ss))}
    ${card('Cultural uses',cc.length?cc.slice(0,5).map(x=>`<div class="wb-entry">${esc(x.region)} · ${esc(x.tradition)}<div class="wb-meta">${esc(x.reported_use)}</div>${linked(x.source_id)}</div>`).join(''):small('No individually sourced cultural uses yet.'))}
    ${card('Folklore / metaphysical beliefs',ff.length?ff.map(x=>`<div class="wb-entry">${esc(x.theme)}<div class="wb-meta">${esc(x.evidence_tier)} · cultural belief, not empirical proof</div>${linked(x.source_id)}</div>`).join(''):small('No published public folklore record yet.'))}
    ${card('Reported chemical inventory',`<p>${os.length} entries; ${os.filter(credibleOccurrence).length} have independently attributed non-legacy occurrence records.</p><p class="wb-meta">Occurrence counts are NOT measured concentrations or interactions.</p>`)}
    </article>`}).join('')}</div>
    <section class="wb-tile wb-shared"><h3>Shared named compounds across selected plants</h3><p class="wb-muted">Inventory similarity only. Verification depends on the specific plant part and analytical source; no inferred medicinal synergy.</p>${shared.length?shared.map(c=>`<div class="wb-entry"><strong>${esc(c.name)}</strong><div class="wb-meta">Appears in ${c.ids.size} selected organisms · ${c.evidence} of ${c.total} occurrence links sourced beyond the legacy inventory</div></div>`).join(''):small('No shared named compounds recorded among the selected plants.')}</section>`;
  }
  function connections(){
    const focusTaxon=names.get(focus)||organisms[0];if(!focusTaxon)return small('No organisms found.');
    const first=occByOrg.get(focusTaxon.id)||[],byComp=new Map(first.map(x=>[x.compound_id,x]));
    const neighbors=organisms.filter(o=>o.id!==focusTaxon.id).map(o=>{const ties=(occByOrg.get(o.id)||[]).filter(x=>byComp.has(x.compound_id)).filter(x=>!verifiedOnly||(credibleOccurrence(x)&&credibleOccurrence(byComp.get(x.compound_id))));return {o,ties};}).filter(r=>r.ties.length).sort((a,b)=>b.ties.length-a.ties.length||a.o.common_name.localeCompare(b.o.common_name));
    return `<div class="wb-controls"><label>Starting organism<select class="wb-input" id="wb-focus">${options(focusTaxon.id)}</select></label><label class="wb-check"><input type="checkbox" id="wb-verified" ${verifiedOnly?'checked':''}> Both organism links must have non-legacy source records</label></div>
    <div class="wb-note"><strong>Compound connections are not binding predictions.</strong> An organism may contain a chemical only in a specific part, extract or concentration. Same-compound links do not demonstrate clinical synergy, medical interchangeability, safety, or a shared treatment effect.</div>
    <h3>Recorded overlaps with ${esc(focusTaxon.common_name)} · ${neighbors.length} other organisms</h3>
    <div class="wb-coverage-list">${neighbors.map(({o,ties})=>`<article class="wb-coverage-row"><div><button class="wb-link" data-open="${esc(o.id)}">${esc(o.common_name)} ↗</button><div class="wb-meta">${esc(o.scientific_name)}</div></div><span class="wb-progress">${ties.length} shared</span><div class="wb-statuses">${ties.slice(0,14).map(x=>`<span class="wb-flag ${credibleOccurrence(x)&&credibleOccurrence(byComp.get(x.compound_id))?'wb-yes':'wb-no'}">${esc(compoundMap.get(x.compound_id)?.display_name||x.compound_id)}</span>`).join('')}${ties.length>14?`<span>+${ties.length-14} more</span>`:''}</div></article>`).join('')||'<div class="wb-muted">No matches under these evidence restrictions. That does not prove there are no shared molecules.</div>'}</div>`;
  }
  function render(){
    holder.innerHTML=`<div class="wb-head"><div><div class="wb-eyebrow">RESEARCH WORKBENCH · Atlas revision ${esc(db.meta?.catalog_revision??'?')}</div><h2>Compare evidence, map chemical connections, see what's missing.</h2><p>Research and cultural reference—not personal dosage instructions or proof of plant efficacy.</p></div><button class="btn" data-close-wb>Return to catalog</button></div>
    <div class="wb-tabs">${[['overview','Coverage dashboard'],['compare','Compare plants'],['connections','Compound connections']].map(([k,label])=>`<button class="btn ${tab===k?'on':''}" data-wb-tab="${k}">${label}</button>`).join('')}</div><div class="wb-body">${tab==='overview'?overview():tab==='compare'?compare():connections()}</div>`;
  }
  holder.addEventListener('click',e=>{
    const target=e.target.closest('button');if(!target)return;
    if(target.hasAttribute('data-close-wb')){hide();return;}
    if(target.dataset.wbTab){tab=target.dataset.wbTab;render();return;}
    if(target.dataset.open){
      const o=names.get(target.dataset.open);if(!o)return;
      document.getElementById('nav-organisms')?.click();
      const input=document.getElementById('search');if(input){input.value=o.scientific_name;input.dispatchEvent(new Event('input',{bubbles:true}));}
      document.querySelector('.layout')?.scrollIntoView({block:'start'});return;
    }
  });
  holder.addEventListener('change',e=>{
    if(e.target.id==='wb-sort'){sort=e.target.value;render();}
    else if(e.target.id==='wb-focus'){focus=e.target.value;render();}
    else if(e.target.id==='wb-verified'){verifiedOnly=e.target.checked;render();}
    else if(e.target.hasAttribute('data-select-compare')){const i=Number(e.target.dataset.selectCompare);if(i>=0&&i<3){selected[i]=e.target.value;render();}}
  });
  holder.addEventListener('input',e=>{
    if(e.target.id==='wb-filter'){filter=e.target.value;const start=e.target.selectionStart;render();const search=holder.querySelector('#wb-filter');search?.focus();if(start!==null)search?.setSelectionRange(start,start);}
  });
})();
