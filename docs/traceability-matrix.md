# Traceability matrix

| Requirement | Module | Evidence | Test |
| --- | --- | --- | --- |
| Candidate profile source-of-truth | `src/careerpilot/profile.py` | Reads `khizar.md` and preserves verification notes | `tests/test_vertical_slice.py` |
| RDF/OWL ontology model | `ontology/careerpilot.ttl` | Core classes, properties, and instance data | `tests/test_vertical_slice.py` |
| SHACL validation | `ontology/shapes.ttl` | Candidate, Evidence, Job, and Application constraints | `tests/test_vertical_slice.py` |
| GraphDB-ready integration | `src/careerpilot/graphdb.py` | `GraphDBClient` with repository-ready query API | `tests/test_vertical_slice.py` |
| SPARQL queries | `ontology/sparql/*.rq` | Skill/evidence and missing-skill retrieval | `tests/test_vertical_slice.py` |
| Job normalization | `src/careerpilot/job.py` | Canonical job record with normalized fields | `tests/test_vertical_slice.py` |
| Explainable matching | `src/careerpilot/match.py` | Skill coverage, evidence, and reasoning output | `tests/test_vertical_slice.py` |
