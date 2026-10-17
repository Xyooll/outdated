"""Prevent regression of the user-approved multidimensional Atlas vision.

This verifies the *planning contract*, not that planned UI/data features exist yet.
Discovered by the existing botanical-atlas-publish.yml unittest invocation.
"""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "PRODUCT_VISION_CONTRACT.json"
REQUIRED = {
    "medicinal", "metaphysical", "active_ingredients",
    "extraction_preparation", "visual_library",
}

class VisionContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = json.loads(CONTRACT.read_text(encoding="utf-8"))

    def test_identity_and_all_nested_families_preserved(self):
        c = self.contract
        self.assertEqual(c["canonical_organism_key"], "organism_id")
        self.assertEqual(c["contract_status"], "approved_vision_not_implemented_features")
        families = c["required_top_level_profiles"]
        self.assertEqual({f["id"] for f in families}, REQUIRED)
        self.assertTrue(all(f["plural"] and f["nesting"] for f in families))
        self.assertIn("tradition", next(f for f in families if f["id"] == "metaphysical")["nesting"])
        self.assertIn("tradition", next(f for f in families if f["id"] == "medicinal")["nesting"])

    def test_provenance_safety_and_media_rights_preserved(self):
        c = self.contract
        self.assertIn("historical_amount_is_not_safe_dose", c["source_boundaries"])
        self.assertIn("tradition_or_spiritual_belief_is_not_clinical_evidence", c["source_boundaries"])
        self.assertIn("extract_is_not_purified_compound", c["source_boundaries"])
        self.assertIn("null_or_negative", c["evidence_tiers"])
        for key in ("source_url", "rights_or_license", "alt_text", "verification_status"):
            self.assertIn(key, c["media_required_fields"])
        self.assertIn("publish_nonpublic_cultural_claims", c["blocked_behaviors"])
        self.assertIn("claim_unbuilt_ui_published", c["blocked_behaviors"])

    def test_release_contract_and_docs_exist(self):
        c = self.contract
        self.assertIn("clove_and_fungus_acceptance", c["release_gates"]["mvp"])
        self.assertIn("existing_v1_6_regression_pass", c["release_gates"]["mvp"])
        for p in ("AGENTS.md", "docs/PROFILE_ARCHITECTURE_VISION.md",
                  "docs/FULL_BUILD_STRATEGY.md", "docs/INGESTION_FORMAT.md"):
            self.assertTrue((ROOT / p).exists(), p)
        strategy = (ROOT / "docs" / "FULL_BUILD_STRATEGY.md").read_text(encoding="utf-8")
        self.assertIn("v1.7", strategy)
        self.assertIn("PRODUCT_VISION_CONTRACT.json", strategy)

    def test_existing_content_not_replaced_by_skeleton(self):
        catalog = json.loads((ROOT / "data" / "atlas.json").read_text(encoding="utf-8"))
        for collection in ("organisms", "medical_systems", "practice_claims", "folklore",
                           "compounds", "bioactivities", "medicinal_materials",
                           "formulas", "formula_components", "interaction_evidence"):
            self.assertIn(collection, catalog, collection)
        self.assertGreaterEqual(len(catalog["organisms"]), 32)
        self.assertGreaterEqual(len(catalog["medical_systems"]), 10)

if __name__ == "__main__":
    unittest.main()
