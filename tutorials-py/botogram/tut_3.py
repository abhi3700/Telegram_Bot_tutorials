"""
    Command arguments parse
    ***********************
    Demo
    ====

    user: 
        /tip tipuser11112 0.1000 EOS restaurant_tip_for_excellent_service
    bot: 
        arg0: tipuser11112
        arg1: 0.1000
        arg2: EOS
        arg3: restaurant_tip_for_excellent_service
    user: 
        /tip
    bot: 
        Please enter tip request (with memo) in this format: /tip RECEIVER_ACCOUNT AMOUNT SYMBOL MEMO 
        (e.g. /tip tipuser11112 0.1000 EOS restaurant_tip_for_excellent_service)
"""

import botogram
from input import *

bot = botogram.create(API_key)    

@bot.command("tip")
def tip_command(chat, message, args):
    """
        Tip your EOSIO token from this bot to a user (with telegram id) along with a memo
        NOTE: Please don't use 'space' in between words in `memo`. Instead, use 'underscore', 'hyphen', etc.
        
        Demo:
        =====
        User: 
            /tip tipuser11112 0.1000 EOS restaurant_tip_for_excellent_service
        Bot:
            DONE!
    """
    if len(args) == 4:
        chat.send(f"arg0: {args[0]}\narg1: {args[1]}\narg2: {args[2]}\narg3: {args[3]}", syntax="plain")        # for testing
    else:
        chat.send("Please enter tip request (with memo) in this format: /tip RECEIVER_ACCOUNT AMOUNT SYMBOL MEMO \n(e.g. /tip tipuser11112 0.1000 EOS restaurant_tip_for_excellent_service)", syntax="plain")

if __name__ == "__main__":
    bot.run()