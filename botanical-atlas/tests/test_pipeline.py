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
    def test_identity_conflict(self):
        with self.assertRaises(ValueError):p.merge(self.data,{'organisms':[{'id':'BOT-001','scientific_name':'Wrong identity'}]})
if __name__=='__main__':unittest.main()
