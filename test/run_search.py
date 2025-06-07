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

if __name__ == "__main__":
    main()
