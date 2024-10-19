from langchain_cohere import CohereEmbeddings
from constants import COHERE_KEY

def get_embedding_model():
    model = CohereEmbeddings(
        model="embed-english-v3.0",
        cohere_api_key=COHERE_KEY
    )
    return model


def get_embeddings_for_query(query):
    model = get_embedding_model()
    embeddings = model.embed_query(query)
    return embeddings
