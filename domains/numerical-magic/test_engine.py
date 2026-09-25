import importlib.util
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("numerical_magic_engine", HERE / "engine.py")
engine = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = engine
SPEC.loader.exec_module(engine)


class NumericalMagicEngineTests(unittest.TestCase):
    def test_reduction_chain_7777(self):
        self.assertEqual(engine.reduction_chain(7777), [7777, 28, 10, 1])

    def test_reduction_chain_38(self):
        self.assertEqual(engine.reduction_chain(38), [38, 11, 2])

    def test_order_is_preserved(self):
        a = engine.analyze_number(38)
        b = engine.analyze_number(83)
        self.assertEqual(a.final_root, b.final_root)
        self.assertNotEqual(a.ordered_path, b.ordered_path)
        self.assertEqual(a.ordered_path, ["Creation", "Manifestation"])
        self.assertEqual(b.ordered_path, ["Manifestation", "Creation"])

    def test_root_family_nine(self):
        family = engine.root_family(9, 5)
        self.assertEqual(family, [9, 18, 27, 36, 45])
        self.assertTrue(all(engine.digital_root(value) == 9 for value in family))

    def test_pythagorean_gpy(self):
        letters, values = engine.pythagorean_values("GPY")
        self.assertEqual(letters, ["G", "P", "Y"])
        self.assertEqual(values, [7, 7, 7])

    def test_gpg_y_chain(self):
        result = engine.analyze_text("GPGY")
        self.assertEqual(result.values, [7, 7, 7, 7])
        self.assertEqual(result.ordinals, [7, 16, 7, 25])
        self.assertEqual(result.glyph_path, ["Gnosis", "Projection", "Gnosis", "Choice"])
        self.assertEqual(result.numeric_analysis.reduction_chain, [7777, 28, 10, 1])
        self.assertEqual(result.ordinal_sum, 55)
        self.assertEqual(result.ordinal_sum_reduction_chain, [55, 10, 1])

    def test_zero_modifier(self):
        result = engine.analyze_number(10)
        self.assertEqual(result.ordered_path, ["Origin", "Potential"])
        self.assertEqual(result.final_root, 1)

    def test_candidates_for_root(self):
        candidates = engine.candidates_for_root(2, digits=2)
        self.assertIn(38, candidates)
        self.assertIn(83, candidates)
        self.assertTrue(all(engine.digital_root(value) == 2 for value in candidates))

    def test_path_permutations(self):
        self.assertEqual(engine.candidates_for_path([3, 8]), [38, 83])
        self.assertEqual(engine.candidates_for_path([3, 8], final_root=2), [38, 83])
        self.assertEqual(engine.candidates_for_path([3, 8], final_root=3), [])

    def test_invalid_root(self):
        with self.assertRaises(ValueError):
            engine.root_family(0)

    def test_w_dual_identity(self):
        value = engine.letter_value("W")
        self.assertEqual(value.ordinal, 23)
        self.assertEqual(value.ordinal_reduction_chain, [23, 5])
        self.assertEqual(value.root, 5)
        self.assertEqual(value.root_name, "Change")

    def test_p_and_y_are_distinct_ordinal_paths_to_seven(self):
        p = engine.letter_value("P")
        y = engine.letter_value("Y")
        self.assertEqual(p.ordinal_reduction_chain, [16, 7])
        self.assertEqual(y.ordinal_reduction_chain, [25, 7])
        self.assertEqual(p.root, 7)
        self.assertEqual(y.root, 7)

    def test_root_five_letter_family_preserves_ordinals(self):
        family = engine.letters_for_root(5)
        self.assertEqual([item.letter for item in family], ["E", "N", "W"])
        self.assertEqual([item.ordinal for item in family], [5, 14, 23])
        self.assertTrue(all(item.root == 5 for item in family))

    def test_dual_channel_word_analysis(self):
        result = engine.analyze_text("WGD")
        self.assertEqual(result.values, [5, 7, 4])
        self.assertEqual(result.root_sequence_surface, "574")
        self.assertEqual(result.numeric_analysis.reduction_chain, [574, 16, 7])
        self.assertEqual(result.ordinals, [23, 7, 4])
        self.assertEqual(result.ordinal_sum, 34)
        self.assertEqual(result.ordinal_sum_reduction_chain, [34, 7])

    def test_letter_options_for_ring(self):
        options = engine.letter_options_for_number(57444)
        self.assertEqual([item.letter for item in options[0]], ["E", "N", "W"])
        self.assertEqual([item.letter for item in options[1]], ["G", "P", "Y"])
        self.assertEqual([item.letter for item in options[2]], ["D", "M", "V"])
        self.assertEqual(len(options), 5)

    def test_zero_requires_declared_symbol_profile(self):
        with self.assertRaises(ValueError):
            engine.letter_options_for_number(10)


if __name__ == "__main__":
    unittest.main()
