import requests
from constants import STACK_OVERFLOW_CLIENT_ID, STACK_OVERFLOW_CLIENT_SECRET, STACK_OVERFLOW_API_KEY
from bs4 import BeautifulSoup
from llm.gemini_utils import get_keywords_from_query
from model.stackoverflow_post import StackOverflowPost

def search_stackoverflow(api_url, params):
    def_params = {
        'order': 'desc',
        'sort': 'relevance',
        'site': 'stackoverflow',
        'answers': 1,
        'key': STACK_OVERFLOW_API_KEY,
        'client_id': STACK_OVERFLOW_CLIENT_ID,
        'client_secret': STACK_OVERFLOW_CLIENT_SECRET,
    }

    def_params.update(params)

    try:

        response = requests.get(api_url, params=def_params)
        response.raise_for_status()

        data = response.json()

        posts = []

        if 'items' in data:
            questions = data['items']
            for question in questions:
                question_id = question['question_id']
                question['answers'] = get_answers(question_id)
                posts.append(StackOverflowPost(question))
            return posts
        else:
            print("No items found.")
            return []

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_answers(question_id):
    """
    Gets the highest voted answer as text.
    :param question_id:
    :return: html escaped answer text
    """
    url = f'https://api.stackexchange.com/2.3/questions/{question_id}/answers'

    params = {
        'order': 'desc',
        'sort': 'votes',
        'site': 'stackoverflow',
        'key': STACK_OVERFLOW_API_KEY,
        'client_id': STACK_OVERFLOW_CLIENT_ID,
        'client_secret': STACK_OVERFLOW_CLIENT_SECRET,
        'filter': 'withbody'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        if 'items' in data:
            answer =  data['items'][0]
            soup = BeautifulSoup(answer['body'], 'html.parser')
            clean_text = soup.get_text().strip()
            return clean_text

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred while fetching answers for question {question_id}: {err}")
        return []
    except Exception as e:
        print(f"An error occurred while fetching answers for question {question_id}: {e}")
        return []


def search_stackoverflow_with_tags(query):
    tags = get_keywords_from_query(query)
    url = 'https://api.stackexchange.com/2.3/search'
    params = {
        'tagged': ";".join(tags)
    }
    return search_stackoverflow(url, params)

def search_stackoverflow_with_query(query):
    url = 'https://api.stackexchange.com/2.3/search/advanced'
    params = {
        'q': query
    }
    return search_stackoverflow(url, params)
