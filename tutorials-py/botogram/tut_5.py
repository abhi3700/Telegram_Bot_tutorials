"""
	button callback
	***********************
	Demo
	====

	user: 
		/addkyc
	bot: 
		Select one of the options below:
		| Name | Address |
	user: 
		<press the Name button>
	bot:
		Please, send your name. E.g.
		kycname Peter Bennett
	user:
		kycname Abhijit Roy
	bot: 
		Abhijit Roy 
		saved.
	=============================================
	user:
		/addkyc

	user: 
		/addkyc
	bot: 
		Select one of the options below:
		| Name | Address |
	user: 
		<press the Address button>
	bot:
		Please, send your address. E.g.

		test bot, [16.05.21 13:49]
		kycaddr 1504 Liberty St.
		New York, NY
		10004 USA
	user:
		kycaddr 508, FF
		Gumni Nagar,
		Mohali, Punjab, 160089
	bot: 
		508, FF
		Gumni Nagar,
		Mohali, Punjab, 160089 
		saved.
"""

import botogram
from input import *

bot = botogram.create(API_key)    

# =============================================================
@bot.command("addkyc")
def spam_command(chat, message, args):
	"""Send a spam message to this chat"""
	btns = botogram.Buttons()
	btns[0].callback("Name", "name")
	btns[0].callback("Address", "address")

	chat.send("Select one of the options below:", attach=btns)

# -------------------------------------------------------------
@bot.callback("name")
def kyc_name_callback(query, chat, message):
	chat.send("Please, send your name. E.g.")
	chat.send("kycname Peter Bennett")

@bot.message_contains("kycname")
def save_kycname(chat, message):
	name = message.text.replace("kycname", "")
	message.reply(f'{name} \nsaved.')

# -------------------------------------------------------------
@bot.callback("address")
def kyc_address_callback(query, chat, message):
	chat.send("Please, send your address. E.g.")
	chat.send("kycaddr 1504 Liberty St.\nNew York, NY\n10004 USA")

@bot.message_contains("kycaddr")
def save_kycaddress(chat, message):
	address = message.text.replace("kycaddr", "")
	message.reply(f'{address} \nsaved.')

# =============================================================
if __name__ == "__main__":
	bot.run()