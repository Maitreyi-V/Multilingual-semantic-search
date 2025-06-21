import os
from search import search_sentence_or_word

def read_all_texts_from_folder(folder_path):
    """
    Reads all .txt files in the given folder and returns:-
    - lines: list of lines /sentences
    - filenames: list of corresponding filenames 
    """
    lines = []
    filenames = []

    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            full_path = os.path.join(folder_path, file)
            with open(full_path, 'r', encoding='utf-8') as f:
                file_lines = f.read().splitlines()
                lines.extend(file_lines)
                filenames.extend([file] * len(file_lines))

    return lines, filenames


def main():
    folder_path = os.path.join(os.path.dirname(__file__), "Examples")
    print(f"Running phrase search in folder: {folder_path}")

    query = input("Enter phrase to search: ").strip()
    if not query:
        print("Empty query.")
        return

    lines, filenames = read_all_texts_from_folder(folder_path)
    if not lines:
        print("No content to search.")
        return

    print("\nMatching results:")
    for i, line in enumerate(lines):
        if search_sentence_or_word(line, query):
            print(f"- [{filenames[i]}] {line}")

if __name__ == "__main__":
    main()
