import datetime
from os import environ


INITIAL_GREET = "Howdy, how are you doing?"

# Options
AVAILABLE_URLS = {
    "/juegos": {
        "/lanzarMoneda": "/tossCoin",
        "/lanzarDado": "/rollDice"
        },
    "/frases": {
        "/mostrarTodasFrases": "/",
        "/fraseAleatoria": "/random"
        }
    }

AVAILABLE_ACTIONS = '\n'.join(list(AVAILABLE_URLS.keys()))
AVAILABLE_GAMES = '\n'.join(list(AVAILABLE_URLS["/juegos"].keys()))
AVAILABLE_PHRASES = '\n'.join(list(AVAILABLE_URLS["/frases"].keys()))

# Mensajes
DEFAULT_MESSAGE = f"Welcome... Date and time: {datetime.datetime.now()}"

# URL's
BASE_API_URL = environ.get('BASE_API_URL', 'http://127.0.0.1:8000/api/v1')

# HTTP Status codes
HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_500_INTERNAL_SERVER_ERROR = 500
