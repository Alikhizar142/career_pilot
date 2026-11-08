from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MatchResult:
    job_id: str
    match_score: float
    eligibility: str
    direct_matches: list[str]
    related_evidence: list[str]
    unsupported_requirements: list[str]
    unknown_requirements: list[str]
    recommendation: str
    explanation: str


def explain_match(candidate_skills: list[str], job_requirements: list[str], job_id: str = "job-001") -> MatchResult:
    required = set(job_requirements)
    candidate = set(candidate_skills)
    direct_matches = sorted(required & candidate)
    missing = sorted(required - candidate)
    score = round(min(100.0, (len(direct_matches) / max(len(required), 1)) * 100), 2)
    eligibility = "eligible" if direct_matches else "uncertain"
    explanation = (
        f"Direct skill coverage is {direct_matches or 'empty'}; missing requirements are {missing or 'none'}; "
        "the score reflects explicit candidate evidence and must not be treated as a hiring probability."
    )
    return MatchResult(
        job_id=job_id,
        match_score=score,
        eligibility=eligibility,
        direct_matches=direct_matches,
        related_evidence=["khizar.md: project and technology evidence"],
        unsupported_requirements=[],
        unknown_requirements=missing,
        recommendation="review" if missing else "strong_candidate",
        explanation=explanation,
    )
