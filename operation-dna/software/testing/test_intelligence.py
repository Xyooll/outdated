from operation_dna.software.intelligence.extract import candidate_mentions
from operation_dna.software.intelligence.resolution import similarity
from operation_dna.software.intelligence.evidence import Evidence, confidence

def test_mentions_are_candidates():
    mentions = candidate_mentions("Acme Corp signed a contract. ACME")
    assert mentions

def test_normalized_similarity():
    assert similarity("Acme Corporation", "Acme Corp") == 1.0

def test_corroboration_increases_confidence():
    one = Evidence("s1", "e1", .8, .2, .8, .8)
    two = Evidence("s2", "e2", .8, .8, .8, .8)
    assert confidence([one, two]) > confidence([one])
