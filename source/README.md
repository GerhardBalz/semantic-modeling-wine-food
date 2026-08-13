# Historical/reference source

## Source corpus

The first reference corpus is the Wine/Food pair from the W3C OWL Web Ontology Language Guide, Recommendation of 10 February 2004.

```text
Guide
https://www.w3.org/TR/2004/REC-owl-guide-20040210/

Wine namespace
http://www.w3.org/TR/2004/REC-owl-guide-20040210/wine#

Food namespace
http://www.w3.org/TR/2004/REC-owl-guide-20040210/food#
```

The guide explains that its examples are based on `wine.rdf` and `food.rdf`, with the Wine ontology importing Food. It also records that the Wine/Food example evolved from earlier description-logic and DAML teaching material.

## Authority boundary

This repository is a reference consumer of that material. It does not claim:

- authorship of the historical Wine/Food semantic model;
- authority over the W3C namespace;
- ownership of the original ontology identifiers;
- that a repository representation would become the canonical ontology.

## Cache/preservation decision

No source bytes are checked in during bootstrap.

A local cache may be added later only when it has a concrete executable purpose such as deterministic reasoning or offline validation. If added, it must:

1. retain historical ontology and entity identity;
2. record the exact retrieval location and timestamp;
3. record a cryptographic digest;
4. record the applicable source licensing terms before redistribution;
5. distinguish the cached representation from semantic authority;
6. provide an upstream-change check separately from deterministic local validation.

This deliberately follows the semantic-identity principle without assuming that the Pizza cache pattern must be copied mechanically.
