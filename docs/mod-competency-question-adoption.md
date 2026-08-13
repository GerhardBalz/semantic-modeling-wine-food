# MOD competency-question adoption

SMO #22 / PR #23 concluded that textual competency questions should reuse the established MOD property `mod:competencyQuestion` rather than introduce a new SMO relation.

The Wine/Food executable example now follows that decision directly:

```text
smwf:MealCourseWineRecommendationModel
    mod:competencyQuestion "Which candidate wines match this meal course and preference profile?"@en
```

The earlier local first-class question resource (`smwf:MealCourseRecommendationQuestion`, `smwf:CompetencyQuestion`, and `smwf:answersQuestion`) has been removed. In this example it carried no identity, lifecycle, provenance, decomposition, or validation semantics beyond the question label, so retaining it would add structure without demonstrated value.

This is useful negative evidence: cross-domain recurrence justifies machine-expressible competency questions, but does not yet justify a reusable resource-valued competency-question relation or class.

No SMO vocabulary changes, SMO↔MOD class alignment, historical W3C Wine/Food identity changes, recommendation-query changes, or `smo:ImplementationProjection` claims are introduced.
