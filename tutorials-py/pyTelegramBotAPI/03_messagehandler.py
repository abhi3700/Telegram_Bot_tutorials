'''
	About
	=====
	Message handler
	---------------
	Send message for a command handler

	Features
	--------
	* A message handler is a function that is decorated with the message_handler decorator of a TeleBot instance. Message handlers consist of one or multiple filters. Each filter much return True for a certain message in order for a message handler to become eligible to handle that message. A message handler is declared in the following way (provided bot is an instance of TeleBot):
	
	```
	@bot.message_handler(filters)
	def function_name(message):
		bot.reply_to(message, "This is a message handler")
	```

	> NOTE: Important: all handlers are tested in the order in which they were declared
'''
import telebot
from input import *

# --------------------About Bot--------------------------------------------------------------------
bot= telebot.TeleBot(token= API_key, parse_mode= None)			# You can set parse_mode by default. HTML or MARKDOWN
bot.about = "This is a Test Bot."
bot.owner = "@abhi3700"

# --------------------------------------------------------------------
# full emoji list - https://apps.timwhitlock.info/emoji/tables/unicode
SOME_FANCY_EMOJI = b'\xf0\x9f\x98\x82'


# --------------------------------------------------------------------
# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	bot.reply_to(message, "Hey buddy!, how are you doing?\nMay I help you with anything?")


# --------------------------------------------------------------------
# Handles all sent text, document, audio, photo  files
@bot.message_handler(content_types=['text', 'document', 'audio', 'photo'])
def handle_text_doc_audio_photo_other(message):
	if message.text:
		bot.reply_to(message, f"text msg detected. and it\'s encoded message: {str(message.text.encode('utf-8'))}")
	elif message.document:
		bot.reply_to(message, f"document file msg detected. & the file_id is \n{message.document[-1].file_id}")
	elif message.audio:
		bot.reply_to(message, f"audio file msg detected. & the file_id is \n{message.audio[-1].file_id}")
	elif message.photo:
		bot.reply_to(message, f"photo msg detected. & the file_id is \n{message.photo[-1].file_id}")
	else:
		bot.reply_to(message, "other file type msg detected.")


# --------------------------------------------------------------------
# Handles all text messages that match the regular expression
@bot.message_handler(regexp="kycdocf")
def handle_message(message):
    bot.reply_to(message, "\'kycdocf\' detected")

# --------------------------------------------------------------------
# Handles all messages for which the lambda returns True
@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def handle_text_doc(message):
	bot.reply_to(message, "text document type msg detected.")

# OR

# Which could also be defined as:
def test_message(message):
	return message.document.mime_type == 'text/plain'

@bot.message_handler(func=test_message, content_types=['document'])
def handle_text_doc(message):
	bot.reply_to(message, "text document type msg detected.")


# --------------------------------------------------------------------
# Handlers can be stacked to create a function which will be called if either message_handler is eligible
# This handler will be called if the message starts with '/hello' OR is some emoji
@bot.message_handler(commands=['hello'])
@bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == SOME_FANCY_EMOJI)
def send_something(message):
    bot.reply_to(message, "hello command or emoji msg detected.")
# --------------------------------------------------------------------
bot.polling()