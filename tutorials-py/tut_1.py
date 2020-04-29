import botogram
from input import *

bot = botogram.create(API_key)    

@bot.command("hello")
def hello_command(chat, message, args):
    """Say hello to the world!"""
    chat.send("What's up bitch")

if __name__ == "__main__":
    bot.run()