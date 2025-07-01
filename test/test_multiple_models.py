import unittest
from semantic_search import semantic_search
from semantic_search_openAI import get_embedding

class TestMultipleModels(unittest.TestCase):
    def setUp(self):
        self.texts = [
            "The soul is eternal",
            "Karma Yoga teaches selfless action",
            "Renunciation is not the mere abandoning of action",
            "He who has conquered himself",
            "The mind is restless and difficult to control",
        ]
        self.queries = [
            "the soul never dies",
            "acting without expecting reward",
        ]
        self.models = [
            "text-embedding-3-small",
            "text-embedding-ada-002",
        ]

    def test_models_on_same_queries(self):
        for model in self.models:
            print(f"\n\nTesting model: {model}")
            embeddings = get_embedding(self.texts, model=model)  # embed once
            for query in self.queries:
                results = semantic_search(query, self.texts, text_embeddings=embeddings, model_name=model)
                print(f"Query: {query}")
                for line, score in results:
                    print(f"  - {line} (Score: {score:.2f})")

if __name__ == "__main__":
    unittest.main()
