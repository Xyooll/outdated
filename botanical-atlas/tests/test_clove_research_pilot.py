"""Clove deep-profile timed research pilot integrity, separate from canonical ingestion."""
import json, pathlib, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
D=ROOT/'data'/'research_pilots'/'clove-deep-dossier.json'
H=ROOT/'site'/'clove-deep-profile.html'
class ClovePilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.d=json.loads(D.read_text('utf-8')); cls.h=H.read_text('utf-8')
    def test_all_five_families_and_nested_profiles(self):
        families={x['id']:x for x in self.d['profile_families']}
        self.assertEqual(set(families),{'medicinal','metaphysical','active_ingredients','extraction_preparation','visual_library'})
        for k in ('medicinal','metaphysical','active_ingredients','extraction_preparation'):
            self.assertGreaterEqual(len(families[k]['profiles']),2)
        self.assertEqual(self.d['status'],'research_pilot_partial_not_full_completion')
        self.assertEqual(self.d['organism_id'],'BOT-001')
    def test_sources_and_cultural_boundaries(self):
        sources={x['id'] for x in self.d['sources']}
        for family in self.d['profile_families']:
            for p in family['profiles']:
                for source in p['source_ids']: self.assertIn(source,sources)
                self.assertGreaterEqual(len(p['fields']),2)
        self.assertIn('not_yet_sourced',{p['evidence'] for f in self.d['profile_families'] for p in f['profiles']})
    def test_photos_licensed_and_identified(self):
        sources={x['id'] for x in self.d['sources']}
        self.assertGreaterEqual(len(self.d['media']),3)
        for m in self.d['media']:
            for k in ('creator','license','license_url','alt','url','source_url'): self.assertTrue(m[k],m['id'])
            self.assertIn(m['source_id'],sources)
            self.assertEqual(m['subject_ref'],'BOT-001')
            self.assertIn(m['id'].replace('VIS-',''),m['id'])
    def test_published_page_and_main_link(self):
        for name in ('Medicinal perspectives','Metaphysical','Active ingredients','Extraction and preparation','Pictures','Ding Xiang','Qaranfal','Lavanga','Eugenol','Research pilot'):
            self.assertIn(name,self.h)
        self.assertIn('clove-deep-profile.html',(ROOT/'app'/'template.html').read_text('utf-8'))
        self.assertIn('<details',self.h)
    def test_canonical_catalog_untouched_by_standalone_research(self):
        original=json.loads((ROOT/'data'/'atlas.json').read_text('utf-8'))
        self.assertEqual(next(x for x in original['organisms'] if x['id']=='BOT-001')['scientific_name'],'Syzygium aromaticum')
        self.assertNotIn('profile_families',original)
if __name__=='__main__':unittest.main()
