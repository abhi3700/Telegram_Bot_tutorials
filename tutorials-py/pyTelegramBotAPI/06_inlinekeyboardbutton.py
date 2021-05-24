'''
	About
	=====
	- one_time_keyboard: the keyboard markup disappears just after pressing a button
	- row_width: no. of buttons in a row. E.g. 2 => max. 2 buttons in a row 

	References
	==========
	- https://github.com/ilteoood/SiteAlert-Python/blob/master/SiteAlert_bot.py

	Example images
	==============
	- button_press_ack.jpg
	- button_press_a_forcereply_ack.jpg
	- button_press_v_forcereply_ack.jpg
	- button_press_d_forcereply_ack.jpg
'''
import telebot
from telebot import types

from input import *

# --------------------About Bot--------------------------------------------------------------------
bot= telebot.TeleBot(token= API_key, parse_mode= None)			# You can set parse_mode by default. HTML or MARKDOWN
bot.about = "This is a Test Bot."
bot.owner = "@abhi3700"

# --------------------------------------------------------------------
gen_markup = types.ReplyKeyboardRemove(selective=False)

# --------------------------------------------------------------------
# M-1:
# @bot.message_handler(commands=["buttons"])
# @bot.message_handler(content_types=['text'])
# def use_button(message):
# 	if message.text == 'a':
# 		bot.reply_to(message, "a is pressed")
# 		bot.send_message(message.chat.id, "Action completed successfully!", reply_markup=gen_markup)
# 	elif message.text == 'v':
# 		bot.reply_to(message, "v is pressed")
#		bot.send_message(message.chat.id, "Action completed successfully!", reply_markup=gen_markup)
# 	elif message.text == 'd':
# 		bot.reply_to(message, "d is pressed")
#		bot.send_message(message.chat.id, "Action completed successfully!", reply_markup=gen_markup)
# 	else:
# 		markup = types.ReplyKeyboardMarkup(one_time_keyboard= True, row_width=2)   # 'one_time_keyboard' hides the keyboard automatically when just after pressing button
# 		# markup = types.ReplyKeyboardMarkup(row_width=2)			# this keeps the keyboard open even after pressing button
# 		itembtn1 = types.KeyboardButton('a')
# 		itembtn2 = types.KeyboardButton('v')
# 		itembtn3 = types.KeyboardButton('d')
# 		markup.add(itembtn1, itembtn2, itembtn3)

# 		bot.send_message(message.chat.id, "Choose one letter: ", reply_markup= markup)


# --------------------------------------------------------------------
# M-2: [RECOMMENDED]
@bot.message_handler(commands=["buttons"])
def use_button(message):
	markup = types.ReplyKeyboardMarkup(one_time_keyboard= True, row_width=2)   # 'one_time_keyboard' hides the keyboard automatically when just after pressing button
	# markup = types.ReplyKeyboardMarkup(row_width=2)			# this keeps the keyboard open even after pressing button
	itembtn1 = types.KeyboardButton('a')
	itembtn2 = types.KeyboardButton('v')
	itembtn3 = types.KeyboardButton('d')
	markup.add(itembtn1, itembtn2, itembtn3)

	msg = bot.send_message(message.chat.id, "Choose one letter: ", reply_markup= markup)
	bot.register_next_step_handler(msg, kbcallback)

def kbcallback(m): 
	if m.text == 'a':
		bot.reply_to(m, "a is pressed")
		# option to enter the name
		markup = types.ForceReply(selective=True)
		msg = bot.send_message(m.chat.id, "Send me your name:", reply_markup=markup)
		bot.register_for_reply(msg, a_callback)
	elif m.text == 'v':
		bot.reply_to(m, "v is pressed")
		markup = types.ForceReply(selective=True)
		msg = bot.send_message(m.chat.id, "Send me your address:", reply_markup=markup)
		bot.register_next_step_handler(msg, v_callback)
	elif m.text == 'd':
		bot.reply_to(m, "d is pressed")
		bot.send_message(m.chat.id, "Action completed successfully!", reply_markup=gen_markup)


def a_callback(m):
	bot.reply_to(m, "Thanks for the name!")

def v_callback(m):
	bot.reply_to(m, "Thanks for the address!")

@bot.message_handler(commands=["removebutton"])
def rm_button(message):
	bot.send_message(message.chat.id, "keyboard markup removed.", reply_markup= rm_kb_markup)


# --------------------------------------------------------------------
# bot.polling(none_stop= True)			# for Production
bot.polling()							# for DEBUG