# ADR 0001: Use ontology-driven candidate modeling

## Status
Accepted

## Context
The initial release requires a trusted representation of a candidate profile, job requirements, and evidence-backed skill assertions. The system must avoid fabricating claims and must keep a clear distinction between skills, assertions, and evidence.

## Decision
We use RDF/OWL modeling with SKOS, PROV-O, and SHACL validation. Candidate facts are ingested from `khizar.md` as assertions with provenance metadata and verification status. Job requirements and candidate evidence are normalized into structured graphs rather than free-form text.

## Consequences
- Advantage: explainable reasoning and traceable evidence.
- Advantage: easier validation and tenant-scoped graph queries.
- Tradeoff: more upfront modeling effort than a simple key-value profile.
- Future work: expand to GraphDB-backed persistence and richer ontology modules.
