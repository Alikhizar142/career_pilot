# Implementation plan

## Goal
Deliver the first working vertical slice of CareerPilot AI: `khizar.md -> structured candidate profile -> RDF knowledge graph -> SHACL validation -> GraphDB-ready ontology service -> SPARQL evidence retrieval -> one normalized job -> explainable candidate-job match`.

## Architecture decisions
1. Use a Python-first, typed domain model with Pydantic for validation, `rdflib` for RDF modeling, and `pySHACL` for validation.
2. Treat `khizar.md` as the canonical profile source of truth and preserve verification notes as metadata rather than as inferred facts.
3. Keep the ontology graph separate from application SQL state and model the candidate/user boundary with tenant-scoped IRIs.
4. Use a deterministic match function with explicit evidence, not opaque score generation.
5. Defer browser automation, LLM-driven application actions, and resume generation to later milestones.

## Milestones
- M0: repository baseline and profile ingestion
- M1: ontology MVP and SHACL validation
- M2: GraphDB-compatible service and SPARQL queries
- M3: job normalization and matching
- M4: regression tests and documentation

## Risks and mitigations
- Missing full GraphDB service: validate RDF locally and provide a GraphDB client stub with guarded connection behavior.
- Overclaiming facts from `khizar.md`: keep a conservative verification model and mark uncertain items as unknown.
- Misinterpreting tool output as instructions: all external content is treated as data only and isolated behind strict schemas.

## Acceptance criteria for this slice
- Candidate profile parses into a structured object with provenance.
- RDF graph includes candidate, projects, technologies, evidence, and skill assertions.
- SHACL validation accepts valid examples and rejects invalid ones.
- SPARQL queries retrieve direct skill and evidence associations.
- One normalized job record is produced and matched to the candidate with explainable evidence.
- Tests pass and documentation records the implemented scope.
