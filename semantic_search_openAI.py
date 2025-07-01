import openai
import numpy as np
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_embedding(text, model="text-embedding-3-small"):
    if isinstance(text, str):
        text = [text]
    text = [t.replace("\n", " ") for t in text]
    response = openai.Embedding.create(input=text, model=model)
    return [np.array(d["embedding"]) for d in response["data"]]