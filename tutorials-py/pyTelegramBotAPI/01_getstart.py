'''
	About
	=====
	print the getMe() response (in JSON)
'''
import telebot
from input import *

# --------------------About Bot--------------------------------------------------------------------
bot= telebot.TeleBot(token= API_key, parse_mode= None)			# You can set parse_mode by default. HTML or MARKDOWN
bot.about = "This is a Test Bot."
bot.owner = "@abhi3700"


print(bot.get_me())