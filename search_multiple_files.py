import os
from semantic_search import semantic_search

def read_all_texts_from_folder(folder_path):
    """
    Reads all .txt files in the given folder and returns a list of tuples:
    (sentence, filename)
    """
    all_lines = []
    file_names = []

    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            path = os.path.join(folder_path, file)
            with open(path, 'r', encoding='utf-8') as f:
                lines = f.read().splitlines()
                all_lines.extend(lines)
                file_names.extend([file] * len(lines))  

    return all_lines, file_names


def main():
    folder = "texts"  
    query = input("Enter search query: ").strip()

    lines, filenames = read_all_texts_from_folder(folder)
    if not lines:
        print("No content to search.")
        return

    top_results = semantic_search(lines, query, top_k=5)

    print("\nTop results across files:")
    for line, score in top_results:
        index = lines.index(line)
        file_origin = filenames[index]
        print(f"- [{file_origin}] {line} (score: {score:.4f})")


if __name__ == "__main__":
    main()
