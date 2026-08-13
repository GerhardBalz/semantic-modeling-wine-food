from pathlib import Path
import unittest
from rdflib import Graph, Literal, Namespace, RDF

ROOT = Path(__file__).resolve().parents[1]
SMO = Namespace("https://w3id.org/smo#")
MOD = Namespace("https://w3id.org/mod#")
SMWF = Namespace("https://w3id.org/semantic-modeling-wine-food/")
PROV = Namespace("http://www.w3.org/ns/prov#")
QUESTION = Literal("Which candidate wines match this meal course and preference profile?", lang="en")
QUERY = """PREFIX smwf: <https://w3id.org/semantic-modeling-wine-food/> SELECT ?wine WHERE { smwf:MainCourseFullBodyRequest smwf:course ?course ; smwf:preferredBody ?body ; smwf:candidateWine ?wine . ?wine a smwf:WineCandidate ; smwf:suitableForCourse ?course ; smwf:hasBody ?body . }"""

class RecommendationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = Graph().parse(ROOT / "models/wine-food-reference.ttl", format="turtle")
        cls.graph.parse(ROOT / "examples/meal-course-wine-recommendation.ttl", format="turtle")

    def test_query_returns_cabernet(self):
        self.assertEqual([r.wine for r in self.graph.query(QUERY)], [SMWF.CabernetCandidate])

    def test_dual_source_lineage(self):
        self.assertEqual(set(self.graph.objects(SMWF.MealCourseWineRecommendationModel, PROV.wasDerivedFrom)), {SMWF.W3COwlGuideWine, SMWF.W3COwlGuideFood})

    def test_competency_question_uses_mod(self):
        self.assertIn((SMWF.MealCourseWineRecommendationModel, MOD.competencyQuestion, QUESTION), self.graph)

    def test_local_question_structure_removed(self):
        self.assertFalse(any(p == SMWF.answersQuestion for p in self.graph.predicates()))

    def test_no_implementation_projection_is_claimed(self):
        self.assertEqual(set(self.graph.subjects(RDF.type, SMO.ImplementationProjection)), set())

    def test_no_explicit_exclusion_relation_is_needed(self):
        self.assertFalse(any(str(p).endswith("excludesElement") for p in self.graph.predicates()))

if __name__ == "__main__":
    unittest.main()
