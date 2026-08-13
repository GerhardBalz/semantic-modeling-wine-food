# Architecture

## Purpose

This repository tests whether the SKE/SMO reference-example pattern generalizes from Pizza to the richer W3C Wine/Food teaching domain without copying Pizza's implementation structure mechanically.

## Source boundary

The historical/reference semantic models remain the W3C OWL Guide Wine and Food models:

```text
Wine
http://www.w3.org/TR/2004/REC-owl-guide-20040210/wine#

Food
http://www.w3.org/TR/2004/REC-owl-guide-20040210/food#
```

The repository does not own those namespaces and does not currently redistribute their source documents.

## First reference architecture

```text
W3C Wine semantic model ───────────┐
                                   │
W3C Food semantic model ───────────┤
                                   ↓
                    repository-authored description
                                   ↓
                      Wine/Food Pairing Reference
                          smo:SemanticModel
                                   ↓
                    future executable proving ground
                  query / validation / reasoning / app
```

The key architectural test is not whether this repository can copy the historical ontologies. It is whether it can model a purpose-specific reference layer while retaining explicit source authority and semantic identity boundaries.

## Modeling question

The initial competency question is:

> Given a meal course and preferences, what semantic information would a recommendation capability need in order to select suitable wines while preserving traceability to the historical Wine/Food source models?

The W3C guide's Wine/Food example is useful because it intentionally joins two semantic domains: Wine imports Food, and the guide discusses meal courses and wine recommendations.

## Artifact distinctions

The bootstrap keeps these categories distinct:

```text
historical semantic model
    Wine and Food source semantics owned externally

repository-authored semantic model description
    metadata describing the source models and local reference model

purpose-specific semantic model
    Wine/Food Pairing Reference Model

implementation projection
    not introduced in bootstrap

runtime data
    not introduced in bootstrap

validation evidence
    deterministic tests over repository-authored metadata

reasoning/query/application artifact
    deferred until source access and concrete executable need justify it
```

This prevents an empty example directory from being mistaken for implemented evidence.

## SMO usage

The governed SMO v0.1 vocabulary is deliberately minimal. The bootstrap therefore uses `smo:SemanticModel` only where justified and relies on established metadata vocabularies such as DCTERMS and PROV-O for source/provenance relationships.

No local requirement is promoted into SMO merely for structural symmetry with Pizza.

## First reusable questions

The Wine/Food example should test whether findings already seen in Pizza recur independently:

1. Do purpose/competency-question relationships need reusable semantic-modeling vocabulary?
2. Is explicit projection scope needed across domains, or only in particular examples?
3. How should a semantic model relate to multiple authoritative source semantic models?
4. When does a representation/cache become necessary for reproducibility rather than merely convenient?
5. Which artifacts are genuinely `smo:ImplementationProjection` rather than generic derived outputs?

Repeated evidence should be raised to SMO or SKE backlog; one example alone is not sufficient to generalize.

## Visibility

The repository remains private during bootstrap review. Public visibility should be reconsidered after:

- source/provenance and licensing treatment is accepted;
- the first executable Wine/Food example exists;
- cross-links with SKE/SMO and Semantic Modeling Pizza are stable.

Visibility does not define semantic authority or maturity.
