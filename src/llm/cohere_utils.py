from langchain_cohere import CohereEmbeddings
from src.constants import COHERE_KEY
import cohere


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


def chat_cohere(system_message, human_message):
    co = cohere.ClientV2(api_key=COHERE_KEY)
    response = co.chat(

        model="command-r-plus-08-2024",

        messages=[{'role': 'system',
                   'content': system_message},
                  {'role': 'user', 'content': human_message}]
        )
    return response
