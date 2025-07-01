from semantic_search_openAI import get_embedding
import numpy as np

def semantic_search(query, texts, text_embeddings=None, top_k=3, model_name="text-embedding-3-small"):
    if not query.strip():
        return []

    query_embedding = get_embedding(query, model=model_name)[0]

    if text_embeddings is None:
        text_embeddings = get_embedding(texts, model=model_name)

    def cosine_similarity(vec1, vec2):
        vec1, vec2 = np.array(vec1), np.array(vec2)
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    similarities = [(text, cosine_similarity(query_embedding, emb)) 
                    for text, emb in zip(texts, text_embeddings)]
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:top_k]
