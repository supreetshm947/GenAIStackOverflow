from datetime import datetime
from llm.cohere_utils import chat_cohere

def convert_timestamp_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp)

def rewrite_query(query):
    system_message = "Rewrite the query, fix all the grammatical error, if required or return the query as it is if everything is correct."
    human_message = query
    response = chat_cohere(system_message, human_message)

    return response.message.content[0].text
