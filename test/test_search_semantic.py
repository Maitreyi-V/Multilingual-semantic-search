"""
Unit tests for the semantic search functionality using OpenAI embeddings.
"""
import sys
import os
import unittest

from semantic_search import semantic_search
from semantic_search_openAI import get_embeddings

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



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
            "He who renounces the fruits of action is wise",

            "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन",
            "योगः कर्मसु कौशलम्",
            "अहिंसा परमो धर्मः",
            "सत्यं वद धर्मं चर",
            "न त्वेवाहं जातु नासं",
            "विद्या ददाति विनयं",
            "मन एव मनुष्याणां कारणं बन्धमोक्षयोः",
            "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन",                    
            "योगस्थः कुरु कर्माणि सङ्गं त्यक्त्वा धनञ्जय",             
            "ज्ञानेन तु तदज्ञानं येषां नाशितमात्मनः",               
            "श्रद्धावान् लभते ज्ञानम्",                              
            "न हि ज्ञानेन सदृशं पवित्रमिह विद्यते",                  
            "सत्त्वं सुखे सञ्जयति",                                 
            "नैव किञ्चित्करोमीति युक्तो मन्येत तत्त्ववित्",          
            "सर्वधर्मान्परित्यज्य मामेकं शरणं व्रज",                
            "अहिंसा परमो धर्मः",                                     
            "विद्या विनयेन शोभते",                                 
            "उद्धरेदात्मनात्मानं",                                   
            "आत्मा वा अरे दृष्टव्यः श्रोतव्यो मन्तव्यो निदिध्यासितव्यः",  
            "यथा दीपो निवातस्थो नेङ्गते सोपमा स्मृता",              
            "न तस्य कार्यं कारणं च विद्यते",                        
            "न हन्यते हन्यमाने शरीरे"  
        ]
        self.model_name = "text-embedding-3-small"
        self.text_embeddings = get_embeddings(self.texts, model=self.model_name)

    def test_relevant_query(self):
        """Test a query that should match a specific relevant sentence."""
        query = "battle confusion"
        result = semantic_search(query, self.texts, self.text_embeddings, model_name=self.model_name)
        self.assertIn("Arjuna was confused about his duty in the war.", [r[0] for r in result])

    def test_spiritual_query(self):
        """Test a query that should match a specific relevant sentence."""
        query = "how to reach liberation"
        result = semantic_search(query, self.texts, self.text_embeddings, model_name=self.model_name)
        self.assertTrue(any("liberation" in r[0].lower() for r in result))

    def test_irrelevant_query(self):
        """Test a query that should match a specific relevant sentence."""
        query = "football game rules"
        result = semantic_search(query, self.texts, self.text_embeddings, model_name=self.model_name)
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
        self.assertTrue(
            any("Renunciation is not the mere abandoning of action" in line for line,
                 _ in results)
                 )

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
        self.assertTrue(
            any("He who has conquered the mind is at peace" in line for line,
                 _ in results)
                 )

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
        self.assertTrue(
            any("He who renounces the fruits of action is wise" in line for line,
                 _ in results)
                 )


    def test_sanskrit_query_nonviolence(self):
        query = "importance of non-violence"
        result = semantic_search(query, self.texts, self.text_embeddings, top_k=3)
        self.assertTrue(any("अहिंसा परमो धर्मः" in line for line, _ in result))

    def test_sanskrit_query_duty(self):
        query = "do your duty but not expect the result"
        result = semantic_search(query, self.texts, self.text_embeddings, top_k=3)
        self.assertTrue(any("कर्मण्येवाधिकारस्ते मा फलेषु कदाचन" in line for line, _ in result))    

        
if __name__ == "__main__":
    unittest.main()
