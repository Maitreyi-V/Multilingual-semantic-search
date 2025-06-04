import unittest
from search import search_sentence_or_word  
class TestSearchFunction(unittest.TestCase):
    def test_basic_query(self):
        text = "hello world\nhi there"
        query = "hello"
        expected_output = ["hello world"]
        self.assertEqual(search_sentence_or_word(text, query), expected_output)

if __name__ == '__main__':
    unittest.main()
