import sys
import os
import unittest

# Ensure semantic_search.py is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from semantic_search import semantic_search

class TestSemanticSearch(unittest.TestCase):
    def setUp(self):
        self.texts = [
            "Arjuna was confused about his duty in the war.",
            "Krishna advised him to act without attachment.",
            "Selfless action is the path to liberation.",
            "The mind is restless and difficult to control.",
            "Yoga is a way to master the mind and senses.",
            "Karma Yoga teaches selfless action",
            "One who sees inaction in action",
            "Renunciation is not the mere abandoning of action",
            "The soul is eternal",
            "He who has conquered himself",
            "Perform your duty without attachment",
            "He who has conquered the mind is at peace",
            "The soul is eternal, indestructible",
            "Be equal in pleasure and pain",
            "He who renounces the fruits of action is wise"
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

    def test_semantic_meaning_match(self):
        query = "selfless action without expecting reward"
        results = semantic_search(self.texts, query)
        self.assertTrue(any("Karma Yoga teaches selfless action" in line for line, _ in results))

    def test_deep_sanskrit_match(self):
        query = "inaction in action"
        results = semantic_search(self.texts, query)
        self.assertTrue(any("One who sees inaction in action" in line for line, _ in results))

    def test_detachment_theme(self):
        query = "giving up results of action"
        results = semantic_search(self.texts, query)
        self.assertTrue(any("Renunciation is not the mere abandoning of action" in line for line, _ in results))

    def test_soul_eternity(self):
        query = "the soul never dies"
        results = semantic_search(self.texts, query)
        self.assertTrue(any("The soul is eternal" in line for line, _ in results))

    def test_inner_strength(self):
        query = "conquering your own mind"
        results = semantic_search(self.texts, query)
        self.assertTrue(any("He who has conquered himself" in line for line, _ in results))

    def test_karma_without_attachment(self):
        query = "action without attachment to results"
        results = semantic_search(self.texts, query)
        self.assertTrue(any("Perform your duty without attachment" in line for line, _ in results))

    def test_mind_mastery(self):
        query = "controlling the mind is self-mastery"
        results = semantic_search(self.texts, query)
        self.assertTrue(any("He who has conquered the mind is at peace" in line for line, _ in results))

    def test_soul_indestructible(self):
        query = "the soul cannot be destroyed by anything"
        results = semantic_search(self.texts, query)
        self.assertTrue(any("The soul is eternal, indestructible" in line for line, _ in results))

    def test_balanced_mind(self):
        query = "treating pleasure and pain the same"
        results = semantic_search(self.texts, query)
        self.assertTrue(any("Be equal in pleasure and pain" in line for line, _ in results))

    def test_sanskrit_to_english_meaning(self):
        query = "renouncing the fruits of action"
        results = semantic_search(self.texts, query)
        self.assertTrue(any("He who renounces the fruits of action is wise" in line for line, _ in results))

if __name__ == "__main__":
    unittest.main()



