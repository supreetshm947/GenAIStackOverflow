from model.stackoverflow_post import StackOverflowPost
from sqlalchemy.exc import NoResultFound
from constants import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_DB, QDRANT_HOST, QDRANT_PORT, QDRANT_COLLECTION_NAME
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from utils import convert_timestamp_to_datetime
from qdrant_client.models import PointStruct
from qdrant_client import QdrantClient

POSTGRES_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}'
QDRANT_URL = f'http://{QDRANT_HOST}:{QDRANT_PORT}'


def get_postgres_session():
    engine = create_engine(POSTGRES_URL)
    session = sessionmaker(bind=engine)()
    return session


def save_to_postgres(stack_overflow_post):
    session = get_postgres_session()
    try:
        session.add(stack_overflow_post)
        session.commit()

    except Exception as e:
        print(f"An error occurred while saving to databases: {e}")
    finally:
        session.close()

def get_post_by_question_id(question_id):
    session = get_postgres_session()

    try:
        post = session.query(StackOverflowPost).filter(StackOverflowPost.question_id == question_id).one()
        return post
    except NoResultFound:
        print(f"No post found with question_id: {question_id}")
        return None
    except Exception as e:
        print(f"An error occurred while retrieving the post: {e}")
        return None
    finally:
        session.close()

def save_vector_to_qdrant(question_id, vector_embedding):
    try:
        client = QdrantClient(url=QDRANT_URL)

        operation_info = client.upsert(
            collection_name=QDRANT_COLLECTION_NAME,
            wait=True,
            points=[
                PointStruct(id=question_id, vector=vector_embedding, payload={})
            ],
        )
        print(operation_info)
    except Exception as e:
        print(f"An error occurred while saving vector to Qdrant: {e}")

def retrieve_similar_vectors(query_vector, threshold=0.7):
    client = QdrantClient(url=QDRANT_URL)
    search_results = client.search(
        collection_name=QDRANT_COLLECTION_NAME,
        query_vector=query_vector,
        limit=5,
        score_threshold=threshold
    )

    return search_results