# Architecture

## Purpose

This repository tests whether the SKE/SMO reference-example pattern generalizes from Pizza to the W3C Wine/Food teaching domain without mechanically copying Pizza's structure.

The central architectural requirement is to preserve historical source authority while authoring a local purpose-specific semantic model and executable recommendation example.

## Source boundary

Historical/reference semantic-model identities remain external:

```text
Wine
http://www.w3.org/TR/2004/REC-owl-guide-20040210/wine#

Food
http://www.w3.org/TR/2004/REC-owl-guide-20040210/food#
```

The repository does not own those namespaces and does not redistribute the original ontology source files.

## Current reference architecture

```text
W3C Wine semantic model ───────────┐
                                   │
W3C Food semantic model ───────────┤
                                   ↓
                     Wine/Food Pairing Reference Model
                         a smo:SemanticModel
                                   ↓
                    Meal-course Recommendation Model
                         a smo:SemanticModel
                                   ↓ exercised by
                    deterministic SPARQL recommendation
```

The local models retain explicit lineage to the historical Wine and Food sources without becoming authorities for those source namespaces.

## Vocabulary boundary

The repository uses:

- governed `smo:SemanticModel` for semantic models;
- DCTERMS and PROV-O for source and derivation relationships;
- MOD `mod:competencyQuestion` for the textual competency question;
- local `smwf:` terms for example-specific recommendation concepts.

No current artifact is classified as `smo:ImplementationProjection`; the experiment has not produced a target-specific implementation-facing projection satisfying that governed definition.

## Executable competency question

The executable question is:

> Which candidate wines match this meal course and preference profile?

`examples/meal-course-wine-recommendation.ttl` records the question with `mod:competencyQuestion`, candidate wines, meal-course/body characteristics, and a concrete request. `tests/test_recommendation.py` runs a deterministic SPARQL query and verifies the expected candidate.

The tests also protect these negative boundaries:

- no `smo:ImplementationProjection` claim;
- no explicit exclusion relation;
- no local first-class competency-question resource.

## Competency-question decision

The first executable experiment used a local resource-valued `smwf:answersQuestion` relation. SMO #22 / PR #23 identified MOD `mod:competencyQuestion` as the established standard for the textual use case.

Wine/Food #5 / PR #6 then tested whether the local question resource added identity/provenance value. It did not, so the local resource/relation were removed. This is negative evidence against creating a resource-valued SMO relation from the current examples.

## Projection/exclusion evidence

Pizza benefits from an explicit local exclusion relation. Wine/Food does not require one: positive selection plus source provenance are sufficient for this bounded recommendation experiment.

The examples are therefore intentionally asymmetric. The lack of a Wine/Food exclusion relation is evidence against promoting Pizza's local relation into SMO.

## Source-cache decision

Unlike Pizza, this executable example does not require local source bytes. A cache should be introduced only if a concrete reproducibility need arises. If added, it must preserve historical semantic identity, record retrieval/integrity/licensing metadata, and remain a representation rather than semantic authority.

## Cross-example result

The completed Pizza ↔ Wine/Food cycle establishes:

- authority/identity stays separate from repository representations;
- multiple-source lineage is adequately modeled with DCTERMS/PROV-O;
- competency questions reuse MOD;
- explicit exclusions remain domain-specific;
- derivation alone does not imply `smo:ImplementationProjection`;
- operation signatures/runtime context/recommendation evidence did not recur as reusable SMO concepts.

No broad SMO or ESKA vocabulary expansion is justified by this cycle.

## Validation

GitHub Actions runs the deterministic Python test suite without network dependency. It verifies historical identifiers, dual-source lineage, the recommendation result, MOD competency-question metadata, and the negative boundaries above.

## Visibility

The source/provenance boundary, executable example, sibling comparison, standards decision, and deterministic validation are stable enough for the visibility decision owned by SKE #29.

Repository visibility does not imply W3C endorsement, authority over historical Wine/Food namespaces, or standardization of local `smwf:` vocabulary.
