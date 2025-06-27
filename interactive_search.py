from semantic_search import semantic_search


texts = [
    "Karma Yoga teaches selfless action",
    "One who sees inaction in action",
    "Renunciation is not the mere abandoning of action",
    "The soul is eternal",
    "He who has conquered himself",
    "Be equal in pleasure and pain",
    "He who renounces the fruits of action is wise"
]

print(" Semantic Search Engine")
print("Type your query below (or type 'exit' to quit):")

while True:
    query = input("\nEnter query: ").strip()
    if query.lower() == "exit":
        print("Goodbye!")
        break

    results = semantic_search(texts, query)
    
    print(f"\nTop Matches for: \"{query}\"")
    for score, line in sorted([(score, line) for line, score in results], reverse=True):
        print(f"Score: {score:.2f}  →  {line}")
