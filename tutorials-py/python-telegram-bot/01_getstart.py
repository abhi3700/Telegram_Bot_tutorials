'''
	About
	=====
	print the getMe() response (in JSON)
'''
import telegram
from input import *

# --------------------About Bot--------------------------------------------------------------------
bot= telegram.Bot(token= API_key)
bot.about = "This is a KYC Bot."
bot.owner = "@abhi3700"


print(bot.get_me())