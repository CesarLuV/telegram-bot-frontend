"""Menu for simple games."""
from typing import Tuple

from utils import api_consumer
from constants import AVAILABLE_URLS


def phrase_selector(phrase_option: str) -> Tuple[str, bool]:
	message = "*Invalid option*"
	phrases_options = AVAILABLE_URLS["/frases"]
	if phrase_option in phrases_options:
		response = api_consumer(f"/frases{phrases_options[phrase_option]}")
		if not response:
			return "_Error in communication with backend API_"
		if AVAILABLE_URLS["/frases"][phrase_option] == '/':
			message = ""
			for item in response:
				message += f'{item["phrase"]}\n*{item["author"]}*\n'
		elif AVAILABLE_URLS["/frases"][phrase_option] == '/random':
			message = f'{response["phrase"]}\n*{response["author"]}*'
	return message
