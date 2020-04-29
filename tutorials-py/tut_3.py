"""
    - channel: @test_keyhubbot
    - user has to be added in this channel
    - The same snippet has been used in @keyhub_bot
"""
import botogram
from input import *

bot = botogram.create(API_key)
bot.about = "This is a practice bot."
bot.owner = "@abhi3700_ofc"

@bot.command("channelstatus")
def channelstatus_command(chat, message, args):
    """shows the channel status of a user - joined or not"""

    # status = bot.api.call("getChatMember", {"chat_id": chat.id, "user_id": message.sender.id})
    status = bot.api.call("getChatMember", {"chat_id": "@test_keyhubbot", "user_id": message.sender.id})    # gives `creator` if you are admin
    
    chat.send("*%s*" % status["ok"])    # gives - True as output
    chat.send("*%s*" % status["result"]["status"])  # gives - creator or member as output

if __name__ == "__main__":
    bot.run()