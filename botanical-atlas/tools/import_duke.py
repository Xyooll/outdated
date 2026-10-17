#!/usr/bin/env python3
"""Pinned, source-attributed USDA Dr Duke CC0 staging. Never infer a treatment or safe dose."""
import argparse,csv,hashlib,io,json,re,unicodedata,zipfile
from pathlib import Path
from collections import Counter,defaultdict
PIN="ff325bc477c355799d12194e2d172c9e181ba44e59056c5ca97f41db595b7d19"
URL="https://catalog.data.gov/dataset/dr-dukes-phytochemical-and-ethnobotanical-databases"
SID="SRC-USDA-DUKE-CSV-CC0-ARCHIVE"
def read(z,name):
    with z.open(name+".csv") as f:
        yield from csv.DictReader(io.TextIOWrapper(f,encoding="utf-8-sig",errors="replace",newline=""))
def norm(s):
    s=unicodedata.normalize("NFKC",str(s)).upper().strip()
    for a,b in {"Α":"ALPHA","Β":"BETA","Γ":"GAMMA"}.items():s=s.replace(a,b)
    return re.sub("[^A-Z0-9]","",s)
def taxon(s):
    s=str(s).split(" (syn.")[0].replace("×"," ").split()
    return " ".join(s[:2]).lower() if len(s)>=2 else ""
def analyze(zip_path,atlas):
    sha=hashlib.sha256(Path(zip_path).read_bytes()).hexdigest()
    if sha!=PIN:raise ValueError("USDA ZIP SHA-256 changed: do not import")
    with zipfile.ZipFile(zip_path) as z:
        if z.testzip() is not None:raise ValueError("Corrupt ZIP")
        required={"FNFTAX.csv","FARMACY_NEW.csv","PARTS.csv","AGGREGAC.csv","ETHNOBOT.csv"}
        if not required.issubset(z.namelist()):raise ValueError("Required USDA table missing")
        if sum(x.file_size for x in z.infolist())>65000000:raise ValueError("Oversized uncompressed archive")
        taxa=defaultdict(list)
        for r in read(z,"FNFTAX"):taxa[taxon(r["TAXON"])].append(r)
        parts={r["PPCO"].strip():r["PPNA"].strip() for r in read(z,"PARTS")}
        mapped={};ambiguous=[]
        for o in atlas["organisms"]:
            if o.get("kingdom")!="Plantae":continue
            matching=taxa.get(taxon(o["scientific_name"]),[])
            if len(matching)==1:
                mapped[matching[0]["FNFNUM"]]={"organism_id":o["id"],"usda_taxon":matching[0]["TAXON"]}
            elif len(matching)>1:ambiguous.append(o["id"])
        chemicals=defaultdict(list)
        for c in atlas["compounds"]:chemicals[norm(c["display_name"])].append(c["id"])
        existing={(r["organism_id"],r["compound_id"]) for r in atlas["occurrences"]}
        candidates=defaultdict(lambda:{"parts":set(),"refs":set(),"names":set(),"rows":0})
        stats=Counter();unmatched=Counter()
        for r in read(z,"FARMACY_NEW"):
            fid=r["FNFNUM"]
            if fid not in mapped:continue
            stats["matched_rows"]+=1
            chem=r["CHEM"].strip();cand=chemicals.get(norm(chem),[])
            if len(cand)!=1:
                if not cand:unmatched[chem]+=1
                else:stats["ambiguous_compound"]+=1
                continue
            key=(mapped[fid]["organism_id"],cand[0])
            if key in existing:stats["existing_chemical_rows"]+=1;continue
            item=candidates[key];item["rows"]+=1;item["names"].add(chem)
            if r["PPCO"].strip():item["parts"].add(parts.get(r["PPCO"].strip(),"Unresolved part "+r["PPCO"].strip()))
            if r["REFERENCE"].strip():item["refs"].add(r["REFERENCE"].strip())
        indexed=[{"organism_id":oid,"compound_id":cid,"parts":sorted(v["parts"]),
          "raw_source_codes":sorted(v["refs"]),"duke_names":sorted(v["names"]),
          "source_rows":v["rows"]} for (oid,cid),v in sorted(candidates.items())]
        names={n for r in indexed for n in r["duke_names"]}
        activities=Counter();ethno=Counter()
        for r in read(z,"AGGREGAC"):
            if r["CHEM"].strip() in names:activities[r["ACTIVITY"].strip()]+=1
        taxa_matched={taxon(r["usda_taxon"]) for r in mapped.values()}
        for r in read(z,"ETHNOBOT"):
            if taxon(r.get("TAXON","")) in taxa_matched:ethno[r["ACTIVITY"].strip()]+=1
        return {"provenance":{"download_url":URL,"sha256":sha,"license":"CC0-1.0",
          "archive_tables":len(z.namelist()),"note":"Archival 2015-2016 CSV, not current authenticated taxonomy"},
          "coverage":{"atlas_plants":sum(x.get("kingdom")=="Plantae" for x in atlas["organisms"]),
          "unambiguous_matched_atlas_plants":len(mapped),"ambiguous_taxa":ambiguous,
          "matched_usda_chemistry_rows":stats["matched_rows"],
          "new_existing_compound_organism_pairs":len(indexed),
          "previously_indexed_source_rows":stats["existing_chemical_rows"],
          "unmatched_compound_rows":sum(unmatched.values()),
          "unmatched_examples":unmatched.most_common(12),
          "activity_labels_NOT_clinical_claims":activities.most_common(12),
          "ethnobotanical_headings_NOT_proven_treatments":ethno.most_common(12)},
          "warnings":["Historical dataset records require verification with original studies.",
          "Activity labels are not assays, clinical efficacy or safe doses.",
          "No metaphysical, extraction yield, image, formula, or medicinal-system attributes inferred."],
          "source_matches":mapped,"candidate_occurrences":indexed}
def pilot(a,limit,oid):
    rs=[x for x in a["candidate_occurrences"] if not oid or x["organism_id"]==oid][:limit]
    if not rs:raise ValueError("No new exact-match candidates")
    source={"id":SID,"organization":"USDA Agricultural Research Service / National Agricultural Library",
      "title":"Dr Duke Phytochemical and Ethnobotanical Databases, archival raw CSV CC0",
      "url":URL,"type":"secondary_historical_compilation_not_primary_chemical_authentication",
      "license":"CC0-1.0","archive_sha256":PIN}
    observations=[]
    for r in rs:
        key=re.sub("[^A-Za-z0-9_-]","_",r["organism_id"]+"-"+r["compound_id"])
        observations.append({"id":"OCC-DUKE-"+key,"organism_id":r["organism_id"],
          "compound_id":r["compound_id"],"source_id":SID,
          "verification":"usda_archival_secondary_unconfirmed",
          "plant_parts":r["parts"],"duke_raw_source_codes":r["raw_source_codes"],
          "duke_rows":r["source_rows"],
          "note":"Historical reported occurrence only. Authentic compound identity, species and assay still require validation; NOT clinical efficacy."})
    return {"batch_id":"20261017_duke_conservative_pilot_001","research_date":"2026-10-17",
      "research_reference_url":URL,"summary":"Limited, explicit unverified source-attributed chemistry reports; no medicinal advice.",
      "sources":[source],"occurrences":observations}
def main():
    p=argparse.ArgumentParser()
    for x in ("archive","atlas","output"):p.add_argument("--"+x,required=True,type=Path)
    p.add_argument("--mode",choices=("audit","batch"),default="audit")
    p.add_argument("--limit",type=int,default=12)
    p.add_argument("--organism-id",default="")
    a=p.parse_args()
    if not 1<=a.limit<=100:p.error("Limit must be 1 to 100")
    report=analyze(a.archive,json.loads(a.atlas.read_text("utf-8")))
    result=report if a.mode=="audit" else pilot(report,a.limit,a.organism_id)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"result":str(a.output),"plants_matched":report["coverage"]["unambiguous_matched_atlas_plants"],
      "candidate_pairs":report["coverage"]["new_existing_compound_organism_pairs"],
      "pilot_rows":len(result.get("occurrences",[]))}))
if __name__=="__main__":main()
