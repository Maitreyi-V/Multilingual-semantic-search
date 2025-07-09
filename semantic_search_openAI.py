from openai import OpenAI
import numpy as np

client = OpenAI()

def get_embeddings(text_list, model="text-embedding-3-small"):
   
    if isinstance(text_list, str):
        text_list = [text_list]

    response = client.embeddings.create(
        input=text_list,
        model=model
    )

    return [np.array(item.embedding) for item in response.data]
