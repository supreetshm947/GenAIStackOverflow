from datetime import datetime
from src.llm.cohere_utils import chat_cohere
from src.api.stackoverflow_utils import search_stackoverflow_with_tags
from src.model.neo4j_utils import insert_so_data


def convert_timestamp_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp)


def rewrite_query(query):
    system_message = "Rewrite the query, fix all the grammatical error, if required or return the query as it is if everything is correct."
    human_message = query
    response = chat_cohere(system_message, human_message)

    return response.message.content[0].text


def escape_curly_braces(input_str):
    escaped_text = input_str.replace("{", "{{")
    escaped_text = escaped_text.replace("}", "}}")
    return escaped_text


def create_vector_index(driver, dimension: int) -> None:
    index_query = "CALL db.index.vector.createNodeIndex('stackoverflow', 'Question', 'embedding', 384, 'cosine')"
    try:
        driver.query(index_query, {"dimension": dimension})
    except Exception as e:  # Already exists
        print(e)
    # index_query = "CALL db.index.vector.createNodeIndex('top_answers', 'Answer', 'embedding', $dimension, 'cosine')"
    # try:
    #     driver.query(index_query, {"dimension": dimension})
    # except:  # Already exists
    #     pass


def create_constraints(driver):
    driver.query(
        "CREATE CONSTRAINT question_id IF NOT EXISTS FOR (q:Question) REQUIRE (q.id) IS UNIQUE"
    )
    driver.query(
        "CREATE CONSTRAINT answer_id IF NOT EXISTS FOR (a:Answer) REQUIRE (a.id) IS UNIQUE"
    )
    # driver.query(
    #     "CREATE CONSTRAINT user_id IF NOT EXISTS FOR (u:User) REQUIRE (u.id) IS UNIQUE"
    # )
    driver.query(
        "CREATE CONSTRAINT tag_name IF NOT EXISTS FOR (t:Tag) REQUIRE (t.name) IS UNIQUE"
    )


def load_so_data_from_tags(neo4j_graph, embedding_model, tags, num_page: int = 1) -> None:
    for i in range(1, num_page + 1):
        response, has_more = search_stackoverflow_with_tags(tags, i)
        insert_so_data(neo4j_graph, embedding_model, response)
        if not has_more:
            break
