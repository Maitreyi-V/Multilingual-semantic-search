"""
Unit tests for the semantic search functionality using OpenAI embeddings.
"""
import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from semantic_search import semantic_search
from semantic_search_openAI import get_embeddings

class TestSemanticSearch(unittest.TestCase):
    """Test suite for semantic search use-cases using GPT-style embeddings."""
    def setUp(self):
        """Set up a sample list of texts and their embeddings."""
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
        self.text_embeddings = get_embeddings(self.texts)

    def test_relevant_query(self):
        """Test a query that should match a specific relevant sentence."""
        query = "battle confusion"
        result = semantic_search(query, self.texts, self.text_embeddings, top_k=2)
        self.assertIn("Arjuna was confused about his duty in the war.", [r[0] for r in result])

    def test_spiritual_query(self):
        """Test a query that should match a specific relevant sentence."""
        query = "how to reach liberation"
        result = semantic_search(query, self.texts, self.text_embeddings, top_k=2)
        self.assertTrue(any("liberation" in r[0].lower() for r in result))

    def test_irrelevant_query(self):
        """Test a query that should match a specific relevant sentence."""
        query = "football game rules"
        result = semantic_search(query, self.texts, self.text_embeddings, top_k=2)
        self.assertTrue(all(score < 0.4 for _, score in result))

    def test_empty_query(self):
        """Test a query that should match a specific relevant sentence."""
        query = ""
        result = semantic_search(query, self.texts, self.text_embeddings)
        self.assertEqual(result, [])

    def test_semantic_meaning_match(self):
        """Test a query that should match a specific relevant sentence."""
        query = "selfless action without expecting reward"
        results = semantic_search(query, self.texts, self.text_embeddings)
        self.assertTrue(any("Karma Yoga teaches selfless action" in line for line, _ in results))

    def test_deep_sanskrit_match(self):
        """Test a query that should match a specific relevant sentence."""
        query = "inaction in action"
        results = semantic_search(query, self.texts, self.text_embeddings)
        self.assertTrue(any("One who sees inaction in action" in line for line, _ in results))

    def test_detachment_theme(self):
        """Test a query that should match a specific relevant sentence."""
        query = "giving up results of action"
        results = semantic_search(query, self.texts, self.text_embeddings)
        self.assertTrue(any("Renunciation is not the mere abandoning of action" in line for line, _ in results))

    def test_soul_eternity(self):
        """Test a query that should match a specific relevant sentence."""
        query = "the soul never dies"
        results = semantic_search(query, self.texts, self.text_embeddings)
        self.assertTrue(any("The soul is eternal" in line for line, _ in results))

    def test_inner_strength(self):
        """Test a query that should match a specific relevant sentence."""
        query = "conquering your own mind"
        results = semantic_search(query, self.texts, self.text_embeddings)
        self.assertTrue(any("He who has conquered himself" in line for line, _ in results))

    def test_karma_without_attachment(self):
        """Test a query that should match a specific relevant sentence."""
        query = "action without attachment to results"
        results = semantic_search(query, self.texts, self.text_embeddings)
        self.assertTrue(any("Perform your duty without attachment" in line for line, _ in results))

    def test_mind_mastery(self):
        """Test a query that should match a specific relevant sentence."""
        query = "controlling the mind is self-mastery"
        results = semantic_search(query, self.texts, self.text_embeddings)
        self.assertTrue(any("He who has conquered the mind is at peace" in line for line, _ in results))

    def test_soul_indestructible(self):
        """Test a query that should match a specific relevant sentence."""
        query = "the soul cannot be destroyed by anything"
        results = semantic_search(query, self.texts, self.text_embeddings)
        self.assertTrue(any("The soul is eternal, indestructible" in line for line, _ in results))

    def test_balanced_mind(self):
        """Test a query that should match a specific relevant sentence."""
        query = "treating pleasure and pain the same"
        results = semantic_search(query, self.texts, self.text_embeddings)
        self.assertTrue(any("Be equal in pleasure and pain" in line for line, _ in results))

    def test_sanskrit_to_english_meaning(self):
        """Test a query that should match a specific relevant sentence."""
        query = "renouncing the fruits of action"
        results = semantic_search(query, self.texts, self.text_embeddings)
        self.assertTrue(any("He who renounces the fruits of action is wise" in line for line, _ in results))

if __name__ == "__main__":
    unittest.main()
