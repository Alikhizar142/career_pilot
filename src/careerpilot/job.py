from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class JobRecord:
    provider: str
    provider_job_id: str
    title: str
    organization: str
    location: str
    workplace_mode: str
    description: str
    required_skills: list[str] = field(default_factory=list)
    preferred_skills: list[str] = field(default_factory=list)
    url: str = ""


def normalize_job(raw_record: dict[str, Any]) -> JobRecord:
    normalized = JobRecord(
        provider=raw_record.get("provider", "example_provider"),
        provider_job_id=str(raw_record.get("provider_job_id", "job-001")),
        title=str(raw_record.get("title", "AI Engineer")),
        organization=str(raw_record.get("organization", "Example Labs")),
        location=str(raw_record.get("location", "Remote")),
        workplace_mode=str(raw_record.get("workplace_mode", "remote")).lower(),
        description=str(raw_record.get("description", "Build AI systems and evaluate model performance.")),
        required_skills=[str(item) for item in raw_record.get("required_skills", [])],
        preferred_skills=[str(item) for item in raw_record.get("preferred_skills", [])],
        url=str(raw_record.get("url", "https://example.com/jobs/ai-engineer")),
    )
    return normalized
