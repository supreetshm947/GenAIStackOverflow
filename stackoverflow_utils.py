import requests
import json
from constants import STACK_OVERFLOW_CLIENT_ID, STACK_OVERFLOW_CLIENT_SECRET, STACK_OVERFLOW_API_KEY
from bs4 import BeautifulSoup


def search_stackoverflow(query):
    url = 'https://api.stackexchange.com//2.3/search/advanced'

    params = {
        'order': 'desc',
        'sort': 'relevance',
        'q': query,
        'site': 'stackoverflow',
        'answers': 1,
        'key': STACK_OVERFLOW_API_KEY,
        'client_id': STACK_OVERFLOW_CLIENT_ID,
        'client_secret': STACK_OVERFLOW_CLIENT_SECRET,
    }

    try:

        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        if 'items' in data:
            questions = data['items']
            for question in questions:
                question_id = question['question_id']
                question['answers'] = get_answers(question_id)
            return questions
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
