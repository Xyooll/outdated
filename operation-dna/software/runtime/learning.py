"""Convert evaluated outcomes into bounded learning records."""
from dataclasses import dataclass
from typing import Any
from .evaluation import EvaluationResult

@dataclass(frozen=True)
class LearningRecord:
    hypothesis: str
    evidence: str
    improvement: float
    accepted: bool
    lesson: str

class LearningEngine:
    def learn(self, hypothesis: str, evaluation: EvaluationResult) -> LearningRecord:
        lesson = evaluation.reason
        if evaluation.candidate_better:
            lesson = f"Candidate validated: {lesson}. Preserve the improvement and retest under new conditions."
        else:
            lesson = f"Candidate rejected: {lesson}. Keep baseline and investigate failure mode."
        return LearningRecord(hypothesis, evaluation.reason, evaluation.improvement, evaluation.candidate_better, lesson)
