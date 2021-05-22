'''
	About
	=====
	Command handler
	---------------
	Send message for a command handler

	Features
	--------
	* A function which is decorated by a message handler can have an arbitrary name, however, it must have only one parameter (the message).
'''
import telebot
from input import *

# --------------------About Bot--------------------------------------------------------------------
bot= telebot.TeleBot(token= API_key, parse_mode= None)			# You can set parse_mode by default. HTML or MARKDOWN
bot.about = "This is a Test Bot."
bot.owner = "@abhi3700"


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hey buddy!, how are you doing?\nMay I help you with anything?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()