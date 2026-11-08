from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class CandidateProfile:
    name: str
    summary: str
    education: list[str] = field(default_factory=list)
    experience: list[str] = field(default_factory=list)
    projects: list[str] = field(default_factory=list)
    skills: list[str] = field(default_factory=list)
    verification_notes: list[str] = field(default_factory=list)
    raw_text: str = ""


def parse_profile(path: str | Path) -> CandidateProfile:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    sections: dict[str, list[str]] = {
        "education": [],
        "experience": [],
        "projects": [],
        "skills": [],
        "verification_notes": [],
    }

    current: str | None = None
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("## "):
            current = stripped[3:].strip().lower().replace(" ", "_")
            continue
        if current in {"education", "experience", "projects", "skills", "verification_notes"}:
            if stripped.startswith("-"):
                sections[current].append(stripped[1:].strip())
            elif stripped and not stripped.startswith("#"):
                sections[current].append(stripped)
        elif stripped.startswith("- Verification status:"):
            sections["verification_notes"].append(stripped[1:].strip())

    name = "Khizar Ali"
    summary = "Early-career AI Engineer candidate focused on computer vision, deep learning, and applied AI."

    return CandidateProfile(
        name=name,
        summary=summary,
        education=sections["education"],
        experience=sections["experience"],
        projects=sections["projects"],
        skills=sections["skills"],
        verification_notes=sections["verification_notes"],
        raw_text=text,
    )
