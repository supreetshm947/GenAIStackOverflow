import requests
import json
from constants import CLIENT_ID, CLIENT_SECRET, KEY


# Replace with your actual credentials
API_KEY = KEY
CLIENT_ID = CLIENT_ID
CLIENT_SECRET = CLIENT_SECRET


def search_stackoverflow(query, pagesize=10):
    # Prepare the API endpoint URL
    url = 'https://api.stackexchange.com/2.3/search'

    # Define the parameters for the API request
    params = {
        'order': 'desc',
        'sort': 'relevance',
        'intitle': query,
        'site': 'stackoverflow',
        'key': API_KEY,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'pagesize': pagesize  # Set the number of items to retrieve
    }

    try:
        # Make the GET request to the Stack Exchange API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the JSON response
        data = response.json()

        # Check if items were returned
        if 'items' in data:
            return data['items']
        else:
            print("No items found.")
            return []

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")

search_stackoverflow("Nvidia GPU")