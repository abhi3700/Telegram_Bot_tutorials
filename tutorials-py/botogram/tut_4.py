"""
	button callback
	***********************
	Demo
	====

	user: 
		/spam
	bot: 
		This is spam!
		| Delete this message |
	user: 
		<press the button>
	bot: 
		Spam message deleted. Sorry!
"""

import botogram
from input import *

bot = botogram.create(API_key)    

@bot.command("spam")
def spam_command(chat, message, args):
	"""Send a spam message to this chat"""
	btns = botogram.Buttons()
	btns[0].callback("Delete this message", "delete")

	chat.send("This is spam!", attach=btns)

@bot.callback("delete")
def delete_callback(query, chat, message):
	message.delete()
	# query.notify("Spam message deleted. Sorry!")
	chat.send("Spam message deleted. Sorry!")
	
if __name__ == "__main__":
	bot.run()