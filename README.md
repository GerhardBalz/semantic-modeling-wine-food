# Semantic Modeling Wine/Food

A Semantic Knowledge Engineering (SKE) reference example for applying the Semantic Modeling Ontology (SMO) to the classic W3C OWL Wine and Food teaching domain.

> **Status:** Public reference baseline complete. The repository is public following the completed SKE #29 publication decision; public visibility is a publication/governance state, not a measure of semantic maturity.

## Role in SKE

This repository is the sibling semantic-modeling reference example to [Semantic Modeling Pizza](https://github.com/GerhardBalz/semantic-modeling-pizza).

Related repositories:

- [Semantic Knowledge Engineering](https://github.com/GerhardBalz/semantic-knowledge-engineering) — initiative architecture and cross-repository governance;
- [Semantic Modeling Ontology](https://github.com/GerhardBalz/semantic-modeling-ontology) — reusable semantic-modeling vocabulary;
- [Semantic Modeling Pizza](https://github.com/GerhardBalz/semantic-modeling-pizza) — first reference example and comparison domain;
- [Pizza Ontology](https://github.com/GerhardBalz/pizza-ontology) — separate preservation/reference proving ground.

This repository does **not** claim authority over the historical W3C Wine or Food namespaces and does not define a successor Wine ontology.

## Historical/reference source

The reference corpus is the Wine/Food ontology pair used by the W3C OWL Web Ontology Language Guide, Recommendation of 10 February 2004:

```text
Wine namespace
http://www.w3.org/TR/2004/REC-owl-guide-20040210/wine#

Food namespace
http://www.w3.org/TR/2004/REC-owl-guide-20040210/food#

Guide
https://www.w3.org/TR/2004/REC-owl-guide-20040210/
```

The repository references this material but does not redistribute the original ontology source files. [`NOTICE.md`](NOTICE.md) and [`source/README.md`](source/README.md) record the authority, provenance, and licensing boundary.

## Reference architecture

```text
W3C Wine semantic model ───────────┐
                                   ├─ source of
W3C Food semantic model ───────────┘
                    Wine/Food Pairing Reference Model
                            smo:SemanticModel
                                   ↓ refined into
                    Meal-course Recommendation Model
                            smo:SemanticModel
                                   ↓ exercised by
                    deterministic SPARQL recommendation
```

Both local semantic models retain explicit lineage to the historical W3C sources without claiming their namespaces.

## Executable recommendation evidence

The repository implements a bounded recommendation question:

> Which candidate wines match this meal course and preference profile?

The textual competency question uses MOD `mod:competencyQuestion`, following the standards-first decision in SMO #22 / PR #23.

A deterministic SPARQL query selects the single candidate matching the example request. The tests also verify:

- lineage to both historical Wine and Food semantic models;
- no `smo:ImplementationProjection` claim;
- no explicit exclusion relation;
- no need for the earlier local first-class competency-question resource.

The last point is intentional negative evidence: the resource was removed because the current example demonstrated no additional identity/provenance value beyond the MOD textual property.

## Vocabulary boundary

The example uses:

- governed `smo:SemanticModel` for semantic models;
- DCTERMS and PROV-O for metadata and lineage;
- MOD `mod:competencyQuestion` for the textual competency question;
- local `smwf:` terms for example-specific recommendation concepts.

No new SMO competency-question term was introduced.

## Repository structure

```text
.
├── .github/workflows/validate.yml
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── NOTICE.md
├── requirements-dev.txt
├── docs/
│   └── architecture.md
├── source/
│   └── README.md
├── models/
│   └── wine-food-reference.ttl
├── examples/
│   └── meal-course-wine-recommendation.ttl
└── tests/
    ├── test_reference_model.py
    └── test_recommendation.py
```

## Validation

Run the deterministic, network-independent validation suite:

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
```

The tests preserve historical identifiers, verify dual-source lineage, execute the recommendation query, require MOD competency-question metadata, and protect the negative `ImplementationProjection` boundary.

## Cross-example findings

The Pizza ↔ Wine/Food comparison produced these outcomes:

- competency-question semantics recur → reuse MOD, not SMO expansion;
- multiple-source lineage → DCTERMS/PROV-O are sufficient;
- explicit exclusions did not recur → no reusable exclusion term justified;
- no `smo:ImplementationProjection` was needed here;
- operation signatures and recommendation-evidence structures did not independently recur at the reusable semantic-modeling layer.

These results are governed in SKE rather than silently generalized here.

## Licensing and attribution

Original repository-authored material is licensed under the MIT License.

Historical W3C Wine/Food material is external reference material and is **not redistributed**. Any future cached/preserved source copy must record the applicable W3C licensing terms before source bytes are committed and must remain a representation rather than replacement semantic identity.

## Governance and visibility

Repository-local semantic evidence belongs here; reusable findings flow to SKE/SMO through standards-first review.

SKE #29 completed the public-visibility decision for this repository and its Pizza sibling. Public visibility does not imply W3C endorsement, authority over historical namespaces, or standardization of local example vocabulary.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the branch, validation, and pull-request workflow.
