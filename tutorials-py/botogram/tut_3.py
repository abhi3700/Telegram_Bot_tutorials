"""
    Command arguments parse
    ************************
    Demo
    ====

    user: 
        /withdrawmemo tipuser11111 1.0000 EOS pay_bill
    bot: 
        arg0: tipuser11111
        arg1: 1.0000
        arg2: EOS
        arg3: pay_bill
"""

import botogram
from input import *

bot = botogram.create(API_key)    

@bot.command("withdrawmemo")
def withdrawmemo_command(chat, message, args):
    """
        Withdraw your EOSIO token from this bot to your EOSIO account with a memo
        NOTE: Please don't use 'space' in between words in `memo`. Instead, use 'underscore', 'hyphen', etc.
        
        Demo:
        =====
        User: 
            /withdrawmemo tipuser11111 1.0000 EOS pay_bill           
    """
    if len(args) == 4:
        chat.send(f"arg0: {args[0]}\narg1: {args[1]}\narg2: {args[2]}\narg3: {args[3]}")        # for testing
    else:
        chat.send("Please enter withdrawal request (with memo) in this format: /withdrawmemo ACCOUNT AMOUNT SYMBOL MEMO \n(e.g. /withdrawmemo tipuser11111 1.0000 EOS pay_bill)")

if __name__ == "__main__":
    bot.run()