def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

if __name__ == "__main__":
    content = read_markdown_file("gita/3-43.md")
    print(content[:500])  

def search_phrase(content, phrase):
    if phrase in content:
        print("Phrase found!")
    else:
        print("Phrase not found.")


phrase_to_search = input("Enter the phrase you want to search for: ")
search_phrase(content, phrase_to_search)

try:
    filename = input("Enter the filename (with extension): ")
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print(" File not found.")
    exit()


if not content.strip():
    print("The file is empty.")
    exit()


phrase_to_search = input("Enter the phrase you want to search for: ").strip()
if not phrase_to_search:
    print("Phrase cannot be empty.")
    exit()


search_phrase(content, phrase_to_search)