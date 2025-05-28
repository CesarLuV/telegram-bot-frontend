"""Menu for simple games."""
from typing import Tuple

from utils import api_consumer
from constants import AVAILABLE_URLS


def game_selector(game_option: str) -> Tuple[str, bool]:
	message = "*Invalid option*"
	available_games = AVAILABLE_URLS["/juegos"]
	if game_option in available_games:
		response = api_consumer(f"/juegos{available_games[game_option]}")
		if not response:
			return "_Error in communication with backend API_"
		if AVAILABLE_URLS["/juegos"][game_option] == '/tossCoin':
			message = f'You got: *{response["side"]}*'
		elif AVAILABLE_URLS["/juegos"][game_option] == '/rollDice':
			message = f'You get a: *{response["number"]}*'
	return message
