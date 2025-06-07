def read_file(file_path):
    """Reads a file and returns its content as a string."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content.strip():
                print("The file is empty.")
                return None
            return content
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
    file_path = input("Enter the file path: ").strip()
    content = read_file(file_path)

    if content:
        phrase = input("Enter the phrase to search: ").strip()
        matches = search_sentence_or_word(content, phrase)

        if matches:
            print("Phrase found in the following lines:")
            for line in matches:
                print("-", line)
        else:
            print("Phrase not found.")
