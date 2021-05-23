'''
	About
	=====
	- Get photo file id & then save it to Redis DB
	- Show image from Redis DB

	Example images
	==============
	- read_photo_save_to_DB.jpg
	- show_img_from_DB.jpg

	NOTE: All the image is saved as 'base64' encoded & then to show the image, just decode it back as 'base64'
'''
import telebot
import redis
import os
import base64

from input import *

# --------------------About Bot--------------------------------------------------------------------
bot= telebot.TeleBot(token= API_key, parse_mode= None)			# You can set parse_mode by default. HTML or MARKDOWN
bot.about = "This is a Test Bot."
bot.owner = "@abhi3700"

# --------------------Redis DB------------------------------------------------------------------------
# define Redis database
r = redis.from_url(REDIS_URL, ssl_cert_reqs=None)		# ssl_verify to false


# --------------------------------------------------------------------
# receive photo with specific captions - kycdocf, kycdocb, selfie
@bot.message_handler(content_types=['photo'])
def receive_photo(message):
	if message.caption == "kycdocf" or message.caption == "kycdocb" or message.caption == "selfie":
		photo_fileid = message.photo[-1].file_id
		# bot.reply_to(message, f"photo msg detected. & the file_id is \n{photo_fileid}")
		# bot.send_photo(message.chat.id, f"{photo_fileid}")

		# get file info & file path
		file_info = bot.get_file(photo_fileid)

		# download from the Telegram server by 
		downloaded_file = bot.download_file(file_info.file_path)

		# with open("new_file.jpg", 'wb') as new_file:				# compressed file, Otherwise use 'png' format
		# Unique file created for each user & delete after use. Otherwise, there will be clash.
		with open(f"img_{message.caption}_{message.chat.id}.jpg", 'wb') as new_file:				
			new_file.write(downloaded_file)

		# send the photo which is downloaded first & then saved
		# bot.send_photo(message.chat.id, open(f"img_{message.caption}_{message.chat.id}.jpg", "rb"))				

		# Saving to Redis DB
		try:
			# encode the image as 'base64' encoding type
			img_encoded = base64.b64encode(open(f"img_{message.caption}_{message.chat.id}.jpg", "rb").read())
			r.set(f"{message.caption}", img_encoded)
			bot.reply_to(message, f"Photo saved to Redis DB.")

		except (redis.exceptions.ConnectionError):
			bot.send_message(message.chat.id, "Sorry! Redis connection error!")

		os.remove(f"img_{message.caption}_{message.chat.id}.jpg")		# delete the file after use

	else:
		bot.reply_to(message, "Caption is not given. Please send again with an acceptable caption: \nkycdocf, kycdocb, selfie")


# --------------------------------------------------------------------
@bot.message_handler(commands=["showf"])
def show_photo(message):
	try:
		if ("kycdocf").encode('utf-8') in r.keys():
			img_data = r.get("kycdocf")			# get the 'base64' encoded image data
			with open(f"img_showf_{message.chat.id}.jpg", "wb") as fh:
				# decode the image as 'base64' encoding type & then write
				fh.write(base64.b64decode(img_data))			
			
			with open(f"img_showf_{message.chat.id}.jpg", 'rb') as photo:
				bot.send_photo(message.chat.id, photo)
			
			os.remove(f"img_showf_{message.chat.id}.jpg")		# delete the file after use
		else:
			bot.reply_to(message, "There is no image for kycdocf")

	except (redis.exceptions.ConnectionError):
		bot.send_message(message.chat.id, "Sorry! Redis connection error!")

# --------------------------------------------------------------------
@bot.message_handler(commands=["showb"])
def show_photo(message):
	try:
		if ("kycdocb").encode('utf-8') in r.keys():
			img_data = r.get("kycdocb")			# get the 'base64' encoded image data
			with open(f"img_showb_{message.chat.id}.jpg", "wb") as fh:
				# decode the image as 'base64' encoding type & then write
				fh.write(base64.b64decode(img_data))			
			
			with open(f"img_showb_{message.chat.id}.jpg", 'rb') as photo:
				bot.send_photo(message.chat.id, photo)
			
			os.remove(f"img_showb_{message.chat.id}.jpg")		# delete the file after use
		else:
			bot.reply_to(message, "There is no image for kycdocb")

	except (redis.exceptions.ConnectionError):
		bot.send_message(message.chat.id, "Sorry! Redis connection error!")

# --------------------------------------------------------------------
@bot.message_handler(commands=["shows"])
def show_photo(message):
	try:
		if ("selfie").encode('utf-8') in r.keys():
			img_data = r.get("selfie");			# get the 'base64' encoded image data
			with open(f"img_shows_{message.chat.id}.jpg", "wb") as fh:
				# decode the image as 'base64' encoding type & then write
				fh.write(base64.b64decode(img_data))			
			
			with open(f"img_shows_{message.chat.id}.jpg", 'rb') as photo:
				bot.send_photo(message.chat.id, photo)
			
			os.remove(f"img_shows_{message.chat.id}.jpg")		# delete the file after use
		else:
			bot.reply_to(message, "There is no image for selfie")

	except (redis.exceptions.ConnectionError):
		bot.send_message(message.chat.id, "Sorry! Redis connection error!")

# --------------------------------------------------------------------
# bot.polling(none_stop= True)			# for Production
bot.polling()							# for DEBUG