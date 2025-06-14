from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_search(texts, query, top_k=3):
    """
    Returns the top_k sentences from texts that semantically match the query.
    """
    if not query.strip():
        return []

    query_embedding = model.encode(query, convert_to_tensor=True)
    text_embeddings = model.encode(texts, convert_to_tensor=True)

    hits = util.semantic_search(query_embedding, text_embeddings, top_k=top_k)[0]

    results = []
    for hit in hits:
        results.append((texts[hit['corpus_id']], float(hit['score'])))
    return results
