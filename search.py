"""Module for searching phrases or words within a block of text."""

def read_file(path_to_file):
    """Reads a file and returns its content as a string."""
    try:
        with open(path_to_file, 'r', encoding='utf-8') as file:
            data = file.read()
            if not data.strip():
                print("The file is empty.")
                return None
            return data
    except FileNotFoundError:
        print("File not found.")
        return None


def search_sentence_or_word(text: str, query: str) -> list:
    """
    Searches for lines in the text that contain the query (case-insensitive).

    Args:
        text (str): Full text content to search in.
        query (str): Phrase or word to search for.

    Returns:
        list: Lines containing the query.
    """
    if not query.strip():
        return []

    lines = text.splitlines()
    query_lower = query.strip().lower()
    return [line.strip() for line in lines if query_lower in line.lower()]


if __name__ == "__main__":
    file_path_input = input("Enter the file path: ").strip()
    file_content = read_file(file_path_input)

    if file_content:
        user_query = input("Enter the phrase to search: ").strip()
        matched_lines = search_sentence_or_word(file_content, user_query)

        if matched_lines:
            print("Phrase found in the following lines:")
            for matched_line in matched_lines:
                print("-", matched_line)
        else:
            print("Phrase not found.")
