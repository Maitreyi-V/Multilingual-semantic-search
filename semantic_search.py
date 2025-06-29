import os
import numpy as np


USE_OPENAI = True

if USE_OPENAI:
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")
    MODEL_NAME = "text-embedding-3-small"
else:
    from sentence_transformers import SentenceTransformer, util
    model = SentenceTransformer('all-mpnet-base-v2')


def get_embedding(texts):
    if USE_OPENAI:
        if isinstance(texts, str):
            texts = [texts]
        response = openai.embeddings.create(input=texts, model=MODEL_NAME)
        return [d.embedding for d in response.data]
    else:
        return model.encode(texts, convert_to_tensor=True)


def semantic_search(texts, query, top_k=3):
    if not query.strip():
        return []

    query_embedding = get_embedding(query)[0]  
    text_embeddings = get_embedding(texts)

    if USE_OPENAI:
        
        def cosine_similarity(vec1, vec2):
            vec1, vec2 = np.array(vec1), np.array(vec2)
            return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

        similarities = [(text, cosine_similarity(query_embedding, emb)) for text, emb in zip(texts, text_embeddings)]
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:top_k]
    else:
        hits = util.semantic_search(query_embedding, text_embeddings, top_k=top_k)[0]
        return [(texts[hit['corpus_id']], float(hit['score'])) for hit in hits]
