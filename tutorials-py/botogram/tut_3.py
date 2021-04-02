"""
    Command arguments parse
    ************************
    Demo
    ====

    user: 
        /withdraw sdf 1.0000 EOS
    bot: 
        arg0: sdf
        arg: 1.0000
        arg2: EOS
"""

import botogram
from input import *

bot = botogram.create(API_key)    

@bot.command("withdraw")
def withdraw_command(chat, message, args):
    """Withdraw your EOSIO token from this bot to your EOSIO account"""
    chat.send(f"arg0: {args[0]}\narg1: {args[1]}\narg2: {args[2]}\n")

if __name__ == "__main__":
    bot.run()