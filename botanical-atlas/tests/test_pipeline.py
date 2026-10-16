import copy, importlib.util, json, pathlib, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('atlas',ROOT/'tools/atlas_pipeline.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
class AtlasTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.data=p.get(ROOT/'data/atlas.json')
    def test_baseline(self):
        # The catalog grows with each successful research batch. Never pin its exact size.
        self.assertTrue(p.check(self.data))
        self.assertGreaterEqual(len(self.data['organisms']),32)
        self.assertGreaterEqual(len(self.data['compounds']),168)
    def test_duplicate_rejection(self):
        d=copy.deepcopy(self.data);d['organisms'].append(d['organisms'][0])
        with self.assertRaises(ValueError):p.check(d)
    def test_bad_compound_reference(self):
        d=copy.deepcopy(self.data)
        d['occurrences'].append({'id':'BAD','organism_id':'BOT-001','compound_id':'not-real'})
        with self.assertRaises(ValueError):p.check(d)
    def test_uncited_chemistry(self):
        b={'batch_id':'20261014_test01','research_date':'2026-10-14','research_reference_url':'https://powo.science.kew.org/','occurrences':[{'id':'BAD'}]}
        with self.assertRaises(ValueError):p.verify(b)
    def test_merge_idempotent(self):
        b={'organisms':[{'id':'BOT-TEST','scientific_name':'Example species','common_name':'Test species'}]}
        initial_count=len(self.data['organisms'])
        d=p.merge(self.data,b)
        self.assertEqual(len(d['organisms']),initial_count+1)
        self.assertTrue(p.check(d))
        self.assertEqual(p.merge(d,b),d)
        self.assertEqual(len(self.data['organisms']),initial_count)
    def test_multisystem_lenses(self):
        self.assertIn('practice_claims',self.data)
        self.assertIn('dose_guidance',self.data)
        self.assertIn('folklore',self.data)
        self.assertIn('regulatory_status',self.data)
        self.assertTrue(p.check(self.data))
        self.assertGreaterEqual(len(self.data['practice_claims']),8)
    def test_broken_medicinal_reference(self):
        d=copy.deepcopy(self.data)
        d['practice_claims'][0]['source_id']='NO-SUCH-SOURCE'
        with self.assertRaises(ValueError):p.check(d)
    def test_reject_universal_safe_dose(self):
        d=copy.deepcopy(self.data)
        d['dose_guidance'][0]['guaranteed_safe']=True
        with self.assertRaises(ValueError):p.check(d)
    def test_reject_restricted_folklore(self):
        d=copy.deepcopy(self.data)
        d['folklore'][0]['public_knowledge']=False
        with self.assertRaises(ValueError):p.check(d)
    def test_browser_javascript_syntax(self):
        # Catch parse failures that Python/schema tests cannot detect.
        import shutil, subprocess
        template=(ROOT/'app/template.html').read_text('utf-8')
        self.assertIn('data-mode="perspectives"',template)
        self.assertIn('function perspectivePanel(',template)
        js=template.rsplit('<script>',1)[1].split('</script>',1)[0]
        if shutil.which('node'):
            result=subprocess.run(['node','--check','-'],input=js,text=True,capture_output=True)
            self.assertEqual(result.returncode,0,result.stderr)
    def test_generated_browser_has_multisystem_content(self):
        html=p.render(self.data).decode('utf-8')
        for expected in ('nav-perspectives','PC-TCM-SCHISANDRA','DG-EMA-GINGER-MOTION','FL-ROSEMARY-REMEMBRANCE'):
            self.assertIn(expected,html)
    def test_workbench_is_embedded_offline(self):
        html=p.render(self.data).decode('utf-8')
        self.assertIn('Research workbench',html)
        self.assertIn('Compare plants',html)
        self.assertIn('Compound connections',html)
        self.assertNotIn('__WB_JS__',html)
        self.assertNotIn('__WB_CSS__',html)
        self.assertNotIn('__EMBED_JSON__',html)
        self.assertIn('aria-pressed="false"',html)
    def test_workbench_data_links_valid(self):
        self.assertTrue(p.check(self.data))
        identities={x['id'] for x in self.data['organisms']}
        self.assertTrue(all(x['organism_id'] in identities for x in self.data['practice_claims']))
        self.assertTrue(all(x['organism_id'] in identities for x in self.data['folklore']))
    def test_bioactivity_records_and_sources(self):
        self.assertGreaterEqual(len(self.data['bioactivities']),8)
        sources={x['id'] for x in self.data['sources']}
        self.assertTrue(all(x['source_id'] in sources for x in self.data['bioactivities']))
        self.assertTrue(p.check(self.data))
    def test_reject_false_eugenol_cure(self):
        d=copy.deepcopy(self.data)
        row=copy.deepcopy(d['bioactivities'][0])
        row['id']='TEST-FALSE-CURE'
        row['human_clinical_efficacy_established']=True
        d['bioactivities'].append(row)
        with self.assertRaises(ValueError):p.check(d)
    def test_reject_missing_activity_source(self):
        d=copy.deepcopy(self.data)
        row=copy.deepcopy(d['bioactivities'][0])
        row['id']='TEST-MISSING-SOURCE'
        row['source_id']='ABSENT-REFERENCE'
        d['bioactivities'].append(row)
        with self.assertRaises(ValueError):p.check(d)
    def test_study_tab_is_rendered(self):
        html=p.render(self.data).decode('utf-8')
        self.assertIn('Study effects',html)
        self.assertIn('ACT-EUG-GIARDIA',html)
        self.assertIn('ACT-CLOVE-GIARDIA-OIL',html)
    def test_medicinal_traditions_are_searchable(self):
        data=self.data
        self.assertGreaterEqual(len(data['practice_claims']),32)
        systems={r['system'] for r in data['practice_claims']}
        self.assertIn('Ayurveda',systems)
        self.assertIn('Traditional Chinese Medicine',systems)
        self.assertIn('Unani / Tibb',systems)
        self.assertIn('Ghanaian traditional herbal medicine',systems)
        self.assertTrue(p.check(data))
    def test_claims_present_in_offline_html(self):
        html=p.render(self.data).decode('utf-8')
        for token in ('>Medicinal claims</button>','medicalSystemGroup(c)','PC-CULTURE-TURMERIC-UNANI','PC-CULTURE-WITHANIA-EAFRICA','Traditional or historical claim'):
            self.assertIn(token,html)
    def test_medical_systems_and_source_specific_axes(self):
        self.assertGreaterEqual(len(self.data['medical_systems']),10)
        byid={s['id']:s for s in self.data['medical_systems']}
        self.assertIn('TCM',byid)
        self.assertIn('AYURVEDA',byid)
        self.assertIn('UNANI',byid)
        self.assertTrue(any(a['id']=='five_phases' for a in byid['TCM']['axes']))
        self.assertTrue(any(a['id']=='dosha' for a in byid['AYURVEDA']['axes']))
        self.assertTrue(any(a['id']=='mizaj' for a in byid['UNANI']['axes']))
        self.assertTrue(p.check(self.data))
    def test_deep_system_profile_must_be_valid(self):
        d=copy.deepcopy(self.data)
        d['practice_claims'][0]['system_id']='UNKNOWN-TRADITION'
        with self.assertRaises(ValueError):p.check(d)
    def test_medical_systems_show_in_offline_app(self):
        html=p.render(self.data).decode('utf-8')
        for token in ('>Medical systems</button>', 'function systemPage(', 'function nativeFramework(', 'WHO'):
            if token!='WHO':self.assertIn(token,html)
    def test_identity_conflict(self):
        with self.assertRaises(ValueError):p.merge(self.data,{'organisms':[{'id':'BOT-001','scientific_name':'Wrong identity'}]})
if __name__=='__main__':unittest.main()
