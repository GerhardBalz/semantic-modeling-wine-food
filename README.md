# Semantic Modeling Wine/Food

A Semantic Knowledge Engineering (SKE) reference example for applying the Semantic Modeling Ontology (SMO) to the classic W3C OWL Wine and Food teaching domain.

> **Status:** Bootstrap reference baseline. The repository is intentionally private while the first modeling and provenance baseline is reviewed. Visibility is a governance decision, not a measure of semantic maturity.

## Role in SKE

This repository is a **Semantic Modeling reference example**.

Related repositories:

- [Semantic Knowledge Engineering](https://github.com/GerhardBalz/semantic-knowledge-engineering) — initiative architecture and cross-repository governance;
- [Semantic Modeling Ontology](https://github.com/GerhardBalz/semantic-modeling-ontology) — owner of reusable semantic-modeling vocabulary;
- [Semantic Modeling Pizza](https://github.com/GerhardBalz/semantic-modeling-pizza) — sibling reference example;
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

The guide describes Wine and Food as an interconnected OWL DL example and uses them to illustrate reasoning about wines, foods, meal courses, grapes, regions and wine recommendations.

No ontology source file is copied into this bootstrap. `source/README.md` records the provenance and licensing boundary that must be resolved before introducing any local cached representation.

## First modeling question

The first reference question is deliberately close to the original OWL Guide use case:

> How can a purpose-specific Wine/Food semantic model retain traceability to the historical Wine and Food semantic models while supporting a wine-for-meal-course recommendation use case without claiming ownership of the source vocabularies?

## Reference chain

```text
W3C OWL Guide Wine semantic model ─┐
                                   ├─ described as SMO semantic models
W3C OWL Guide Food semantic model ─┘
                 ↓ source of
Wine/Food Pairing Reference Model
        smo:SemanticModel
                 ↓ exercised by
pairing-oriented query / validation examples
```

The bootstrap intentionally uses only the published SMO class `smo:SemanticModel`. It does not invent new SMO properties for relationships that are not yet part of the governed vocabulary.

## Repository structure

```text
.
├── .github/workflows/validate.yml
├── README.md
├── LICENSE
├── NOTICE.md
├── requirements-dev.txt
├── docs/
│   └── architecture.md
├── source/
│   └── README.md
├── models/
│   └── wine-food-reference.ttl
└── tests/
    └── test_reference_model.py
```

Additional directories such as `examples/`, `queries/`, `shapes/` or `data/` should be added only when an executable example justifies them.

## Validation

Install the single development dependency and run:

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
```

The test parses the Turtle model and checks the minimum semantic and provenance contract deterministically without network access.

## Licensing and attribution

Original repository-authored material is licensed under the MIT License.

Historical W3C Wine/Food material is external reference material and is **not redistributed in this bootstrap**. Its source, attribution and licensing boundary are documented in `NOTICE.md` and `source/README.md`. Any future cache or preserved representation must record the applicable W3C licensing terms before source bytes are committed.

## Governance

Repository-local work is tracked in [issue #1](https://github.com/GerhardBalz/semantic-modeling-wine-food/issues/1). Reusable findings should flow upward rather than being silently generalized:

- cross-repository engineering/governance → SKE;
- reusable semantic-modeling vocabulary → SMO;
- domain-specific Wine/Food evidence → this repository.
