"""Archivo principal de ejecucion del bot."""
import os

import telebot

import gaming_actions as ga
import phrase_actions as pa
import constants as cte


BOT_TOKEN = os.environ.get('BOT_TOKEN', "")

bot = telebot.TeleBot(BOT_TOKEN)


def game_selector(message):
	game_option = message.text
	response = ga.game_selector(game_option)
	bot.send_message(message.chat.id, response, parse_mode="Markdown")


def phrase_selector(message):
	phrase_option = message.text
	response = pa.phrase_selector(phrase_option)
	bot.send_message(message.chat.id, response, parse_mode="Markdown")


@bot.message_handler(commands=['start'])
def send_welcome(message):
	text = f"{cte.INITIAL_GREET}\nEstas son mis acciones disponibles:\n{cte.AVAILABLE_ACTIONS}"
	bot.reply_to(message, text)


@bot.message_handler(commands=['juegos'])
def action_handler(message):
	text = f"Juegos\nElige un juego:\n{cte.AVAILABLE_GAMES}"
	bot.reply_to(message, text)


@bot.message_handler(commands=['frases'])
def action_handler(message):
	text = f"Frases\nElige una accion:\n{cte.AVAILABLE_PHRASES}"
	bot.reply_to(message, text)


@bot.message_handler(commands=cte.AVAILABLE_GAMES.replace('\n', '').split('/'))
def game_handler(message):
	game_selector(message)


@bot.message_handler(commands=cte.AVAILABLE_PHRASES.replace('\n', '').split('/'))
def phrase_handler(message):
	phrase_selector(message)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
	bot.reply_to(message, message.text)


# Last line, starts the bot and keeps listening.
bot.infinity_polling()
