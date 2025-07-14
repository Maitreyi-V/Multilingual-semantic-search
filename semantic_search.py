import numpy as np
from semantic_search_openAI import get_embeddings

def cosine_similarity(vec1, vec2):
    vec1, vec2 = np.array(vec1), np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def semantic_search(query, texts, text_embeddings=None, top_k=3, model_name=None):
    if not query.strip():
        return []

    embedding_model = model_name or "text-embedding-3-small"

    query_embedding = get_embeddings(query, model=embedding_model)[0]

    if text_embeddings is None:
        text_embeddings = get_embeddings(texts, model=embedding_model)

    similarities = [
        (text, cosine_similarity(query_embedding, emb))
        for text, emb in zip(texts, text_embeddings)
    ]

    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:top_k]
