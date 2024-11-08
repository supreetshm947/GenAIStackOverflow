import requests
from src.constants import STACK_OVERFLOW_CLIENT_ID, STACK_OVERFLOW_CLIENT_SECRET, STACK_OVERFLOW_API_KEY
from bs4 import BeautifulSoup
from src.llm.gemini_utils import get_keywords_from_query

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
        has_more = data["has_more"] if "has_more" in data else False
        if 'items' in data:
            questions = data['items']
            for question in questions:
                question_id = question['question_id']
                question['answers'] = get_answers(question_id)
                posts.append(question)
            return posts, has_more
        else:
            print("No items found.")
            return [], has_more

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
        'filter': 'withbody',
        'pagesize':100
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        answers = []
        if 'items' in data:
            for response in data['items']:
                answer =  response
                soup = BeautifulSoup(answer['body'], 'html.parser')
                answer['body'] = soup.get_text().strip()
                answers.append(answer)

        return answers

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred while fetching answers for question {question_id}: {err}")
        return []
    except Exception as e:
        print(f"An error occurred while fetching answers for question {question_id}: {e}")
        return []


def search_stackoverflow_with_tags(query, page):
    tags = get_keywords_from_query(query)
    url = 'https://api.stackexchange.com/2.3/search'
    params = {
        'tagged': ";".join(tags),
        'page':page
    }
    return search_stackoverflow(url, params)

def search_stackoverflow_with_query(query, page):
    url = 'https://api.stackexchange.com/2.3/search/advanced'
    params = {
        'q': query,
        'page':page
    }
    return search_stackoverflow(url, params)
