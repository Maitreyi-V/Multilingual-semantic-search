import unittest
from search import search_sentence_or_word

class TestSearchFunction(unittest.TestCase):
    def test_basic_query(self):
        text = "hello world\nhi there"
        query = "hello"
        expected_output = ["hello world"]
        self.assertEqual(search_sentence_or_word(text, query), expected_output)

    def test_substring_match(self):
        text = "karma yoga is important\nbhakti yoga\nKARMA rules"
        query = "karma"
        matches = search_sentence_or_word(text, query)
        self.assertTrue(all("karma" in line.lower() for line in matches))

    def test_devanagari_word(self):
        text = "कर्म ही धर्म है\nज्ञान श्रेष्ठ है"
        query = "कर्म"
        matches = search_sentence_or_word(text, query)
        self.assertTrue(all("कर्म" in line for line in matches))

    def test_no_match(self):
        text = "this is some text"
        query = "banana"
        matches = search_sentence_or_word(text, query)
        self.assertEqual(matches, [])

    def test_empty_query(self):
        text = "some content here"
        query = ""
        matches = search_sentence_or_word(text, query)
        self.assertEqual(matches, [])

    def test_leading_trailing_spaces_in_query(self):
        text = "karma is a law"
        query = "  karma  "
        matches = search_sentence_or_word(text, query)
        self.assertTrue(all("karma" in line.lower() for line in matches))

    def test_special_characters(self):
        text = "karma, dharma."
        query = "karma,"
        matches = search_sentence_or_word(text, query)
        self.assertTrue(all("karma" in line.lower() for line in matches))

if __name__ == "__main__":
    unittest.main()
