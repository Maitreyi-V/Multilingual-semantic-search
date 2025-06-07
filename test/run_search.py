from processor import search_phrase

def main():
   
    with open("sample.txt", "r") as f:
        content = f.read()

    phrase = input("Enter a phrase to search: ")
    result = search_phrase(content, phrase)

    if result:
        print("Phrase found")
    else:
        print("Phrase not found!")

def search(query, file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return [line.strip() for line in lines if query.lower().strip() in line.lower()]

y
if __name__ == "__main__":
    main()
