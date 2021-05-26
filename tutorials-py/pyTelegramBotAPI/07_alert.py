'''
	About
	=====
	- alert when clicked an inline keyboard

	References
	==========
	- 

	Example images
	==============
	- inlinekeyboard_alert.png
'''
import telebot
from telebot import util,types

from input import *

# --------------------About Bot--------------------------------------------------------------------
bot= telebot.TeleBot(token= API_key, parse_mode= None)			# You can set parse_mode by default. HTML or MARKDOWN
bot.about = "This is a Test Bot."
bot.owner = "@abhi3700"


# --------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def starting_point(message):
    mkup = types.InlineKeyboardMarkup(row_width=2)
    itembtn1 = types.InlineKeyboardButton("A", callback_data="A")
    itembtn2 = types.InlineKeyboardButton("B", callback_data="B")
    mkup.add(itembtn1, itembtn2)
    text = "Hello! Choose one option"
    bot.send_message(message.chat.id, text, reply_markup=mkup)


@bot.callback_query_handler(func=lambda call: call.data == 'A')
def a_choosen(call):
    bot.answer_callback_query(call.id, text= "This is about entering name", show_alert=True, )
    

@bot.callback_query_handler(func=lambda call: call.data == 'B')
def b_choosen(call):
    mkup = types.InlineKeyboardMarkup(row_width=1)
    itembtn1 = types.InlineKeyboardButton("Back", callback_data="back")
    mkup.add(itembtn1)
    text = "You chose B"
    bot.edit_message_text( text, call.message.chat.id, call.message.message_id, reply_markup=mkup)

@bot.callback_query_handler(func=lambda call: call.data == 'back')
def back_choosen(call):
    mkup = types.InlineKeyboardMarkup(row_width=2)
    itembtn1 = types.InlineKeyboardButton("A", callback_data="A")
    itembtn2 = types.InlineKeyboardButton("B", callback_data="B")
    mkup.add(itembtn1, itembtn2)
    text = "Hello again! Choose one."
    bot.edit_message_text( text, call.message.chat.id, call.message.message_id, reply_markup=mkup)

# --------------------------------------------------------------------
# bot.polling(none_stop= True)			# for Production
bot.polling()							# for DEBUG