from __future__ import annotations

from pathlib import Path

from careerpilot.graphdb import GraphDBClient
from careerpilot.job import normalize_job
from careerpilot.match import explain_match
from careerpilot.profile import parse_profile


def test_parse_profile_reads_khizar_source_of_truth():
    profile = parse_profile(Path("khizar.md"))
    assert profile.name == "Khizar Ali"
    assert "BS Artificial Intelligence" in profile.education[0]
    assert "PyTorch" in profile.skills
    assert "LangChain" in profile.skills
    assert any("verification" in note.lower() for note in profile.verification_notes)


def test_graphdb_client_has_safe_stub_api():
    client = GraphDBClient()
    result = client.query("SELECT * WHERE { ?s ?p ?o } LIMIT 10")
    assert result[0]["status"] == "simulated"
    assert client.ping() is True


def test_normalize_job_record():
    record = normalize_job({
        "provider": "example_provider",
        "provider_job_id": "job-001",
        "title": "AI Engineer",
        "organization": "Example Labs",
        "location": "Remote",
        "workplace_mode": "remote",
        "description": "Build AI systems and evaluate model performance.",
        "required_skills": ["Python", "PyTorch", "Deep Learning"],
        "preferred_skills": ["MLOps", "FastAPI"],
        "url": "https://example.com/jobs/ai-engineer",
    })
    assert record.workplace_mode == "remote"
    assert record.required_skills[0] == "Python"


def test_explain_match_is_conservative_and_traceable():
    match = explain_match(
        candidate_skills=["Python", "PyTorch", "OpenCV", "FastAPI"],
        job_requirements=["Python", "PyTorch", "Deep Learning", "MLOps"],
        job_id="job-001",
    )
    assert match.job_id == "job-001"
    assert match.direct_matches == ["PyTorch", "Python"]
    assert match.eligibility in {"eligible", "uncertain"}
    assert "khizar.md" in match.related_evidence[0]
    assert "unknown_requirements" in match.__dict__
