import botogram

API_key = "885410871:AAHb_lwnzFQ2jci_6W_NVgJSUSAUQN_skns"

bot = botogram.create(API_key)    

@bot.command("hello")
def hello_command(chat, message, args):
    """Say hello to the world!"""
    chat.send("What's up bitch")

if __name__ == "__main__":
    bot.run()