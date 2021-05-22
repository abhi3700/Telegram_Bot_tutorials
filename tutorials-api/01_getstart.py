'''
	About
	=====
	print the getMe() response (in JSON)
'''
import requests
from input import *

# --------------------About Bot--------------------------------------------------------------------
bot_get_me = requests.get('https://api.telegram.org/bot{API_key}/{method}'.format(API_key=API_key, method= 'getMe'))
# bot.about = "This is a Test Bot."
# bot.owner = "@abhi3700"


print(bot_get_me.text)