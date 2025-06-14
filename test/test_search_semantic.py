import unittest
from semantic_search import semantic_search

class TestSemanticSearch(unittest.TestCase):
    def setUp(self):
        self.texts = [
            "Arjuna was confused about his duty in the war.",
            "Krishna advised him to act without attachment.",
            "Selfless action is the path to liberation.",
            "The mind is restless and difficult to control.",
            "Yoga is a way to master the mind and senses."
        ]

    def test_relevant_query(self):
        query = "battle confusion"
        result = semantic_search(self.texts, query, top_k=2)
        self.assertIn("Arjuna was confused about his duty in the war.", [r[0] for r in result])

    def test_spiritual_query(self):
        query = "how to reach liberation"
        result = semantic_search(self.texts, query, top_k=2)
        self.assertTrue(any("liberation" in r[0].lower() for r in result))

    def test_irrelevant_query(self):
        query = "football game rules"
        result = semantic_search(self.texts, query, top_k=2)
   
        self.assertTrue(all(score < 0.4 for _, score in result))

    def test_empty_query(self):
        query = ""
        result = semantic_search(self.texts, query)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()



