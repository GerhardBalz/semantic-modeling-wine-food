from pathlib import Path
import unittest

from rdflib import Graph, Namespace, RDF, URIRef

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "models" / "wine-food-reference.ttl"

SMO = Namespace("https://w3id.org/smo#")
SMWF = Namespace("https://w3id.org/semantic-modeling-wine-food/")
DCTERMS = Namespace("http://purl.org/dc/terms/")
PROV = Namespace("http://www.w3.org/ns/prov#")

WINE_ID = URIRef("http://www.w3.org/TR/2004/REC-owl-guide-20040210/wine#")
FOOD_ID = URIRef("http://www.w3.org/TR/2004/REC-owl-guide-20040210/food#")
GUIDE = URIRef("https://www.w3.org/TR/2004/REC-owl-guide-20040210/")


class WineFoodReferenceModelTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = Graph().parse(MODEL, format="turtle")

    def test_three_semantic_models_are_declared(self):
        semantic_models = set(self.graph.subjects(RDF.type, SMO.SemanticModel))
        self.assertEqual(
            semantic_models,
            {
                SMWF.W3COwlGuideWine,
                SMWF.W3COwlGuideFood,
                SMWF.WineFoodPairingReferenceModel,
            },
        )

    def test_historical_identifiers_remain_external(self):
        self.assertIn(
            WINE_ID,
            self.graph.objects(SMWF.W3COwlGuideWine, DCTERMS.identifier),
        )
        self.assertIn(
            FOOD_ID,
            self.graph.objects(SMWF.W3COwlGuideFood, DCTERMS.identifier),
        )
        self.assertIn(GUIDE, self.graph.objects(SMWF.W3COwlGuideWine, DCTERMS.source))
        self.assertIn(GUIDE, self.graph.objects(SMWF.W3COwlGuideFood, DCTERMS.source))

    def test_pairing_model_traces_to_both_sources(self):
        derived_from = set(
            self.graph.objects(SMWF.WineFoodPairingReferenceModel, PROV.wasDerivedFrom)
        )
        self.assertEqual(
            derived_from,
            {SMWF.W3COwlGuideWine, SMWF.W3COwlGuideFood},
        )


if __name__ == "__main__":
    unittest.main()
