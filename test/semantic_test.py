from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_search(texts, query, top_k=3):
    """
    Returns the top_k sentences from texts that semantically match the query.
    """
    query_embedding = model.encode(query, convert_to_tensor=True)
    text_embeddings = model.encode(texts, convert_to_tensor=True)

    hits = util.semantic_search(query_embedding, text_embeddings, top_k=top_k)[0]

    results = []
    for hit in hits:
        results.append((texts[hit['corpus_id']], float(hit['score'])))
    return results

if __name__ == "__main__":
    strings = [
        "Arjuna was confused about his duty in the war.",
        "Krishna advised him to act without attachment.",
        "Selfless action is the path to liberation.",
        "The mind is restless and difficult to control."
    ]

    search_phrase = input("Enter your search phrase: ")
    matches = semantic_search(strings, search_phrase)

    print("\nTop semantic matches:")
    for text, score in matches:
        print(f"- {text} (score: {score:.4f})")
