'''Utilities.'''
import requests

from constants import BASE_API_URL, HTTP_200_OK, HTTP_201_CREATED


def api_consumer(action: str) -> str:
    try:
        r = requests.get(f'{BASE_API_URL}{action}')
        json_response = r.json()
        if r.status_code not in (HTTP_200_OK, HTTP_201_CREATED):
            raise Exception(json_response['detail'])
    except Exception as e:
        print(f"Something went wrong: {e}")
        json_response = None

    return json_response
