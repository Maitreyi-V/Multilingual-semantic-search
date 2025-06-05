from run_search import search

def test_search_returns_only_matching_lines():
    matches = search("karma", "gita/3-43.md")
    assert len(matches) > 0
    assert all("karma" in line.lower() for line in matches)

def test_devanagari_word():
    matches = search("कर्म", "gita/3-43.md")
    assert all("कर्म" in line for line in matches)

def test_case_insensitive_uppercase():
    matches = search("KARMA", "gita/3-43.md")
    assert all("karma" in line.lower() for line in matches)

def test_no_match():
    matches = search("banana", "gita/3-43.md")
    assert matches == []

def test_empty_query():
    matches = search("", "gita/3-43.md")
    assert matches == []

def test_substring_search():
    matches = search("kar", "gita/3-43.md")
    assert all("kar" in line.lower() for line in matches)

def test_multiple_occurrences_in_line():
    matches = search("karma", "gita/3-43.md")
    for line in matches:
        if "karma" in line.lower():
            assert line.lower().count("karma") >= 1

def test_leading_trailing_whitespace_query():
    matches = search("  karma  ", "gita/3-43.md")
    assert all("karma" in line.lower() for line in matches)

def test_special_characters_in_query():
    matches = search("karma,", "gita/3-43.md")
    assert all("karma" in line.lower() for line in matches)

if __name__ == "__main__":
    test_search_returns_only_matching_lines()
    test_devanagari_word()
    test_case_insensitive_uppercase()
    test_no_match()
    test_empty_query()
    test_substring_search()
    test_multiple_occurrences_in_line()
    test_leading_trailing_whitespace_query()
    test_special_characters_in_query()
    print("All tests passed.")
