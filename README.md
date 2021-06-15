# Telegram_Bot_tutorials
Learn how to make a telegram bot from basics to sample bots

## Bot Types in Telegram
* __Normal:__
  - It can be added to a group for multiple people to access at a time.
* __Inline:__
  - No need to add into any group
  - Access via `@bot1` in the message box

## Bot features (using Python)
* [x] Add inline keyboards: contact, location, custom
* [x] Add buttons
* [x] Attach to Database
* [ ] Add to a group
* [ ] Verify a bot/human: by sending direct message to that user & check for clicking a button
* [ ] Create a UI with back button, options like an App

## Programming
### Python
* [my python tutorials](./tutorials-py)
* Python-telegram-bot - [Github](https://github.com/python-telegram-bot/python-telegram-bot)
* PyTelegramBotAPI - [Github](https://github.com/eternnoir/pyTelegramBotAPI)
* Botogram (Python framework for Telegram bots) - [Github](https://botogram.dev/), [Telegram API wrapper](https://botogram.dev/docs/0.6.1/api/telegram/), [Bots Creation API](https://botogram.dev/docs/0.6.1/api/bot/)
	> NOTE: Look for latest version
	- [Small example for botogram "normal" keyboards](https://gist.github.com/MarcoBuster/8f9e7661006436af39c797f02a3d48cc)
	- [A very small script to send text or files over Telegram by using CLI](https://gist.github.com/MarcoBuster/8e4f6db4dc4ba5eb5640224b518d7c7e)
  - [Check if a user is member of channel](https://github.com/python-botogram/botogram/issues/145)
  - [Get User's username in a chat with Telegram Bot](https://github.com/python-botogram/botogram/issues/137#)
  - [Added support for function annotations](https://gist.github.com/hearot/e00bd75312a781c4a20db1131585cd38)
  - Examples Bots (built on Botogram framework)
    + [botogramQBittorrent](https://github.com/ch3p4ll3/botogramQBittorrent)
    + [ban_binance_spamimages](https://github.com/ch3p4ll3/binanceban)
    + [Reminder Bot](https://github.com/Mamiglia/Reminder-Bot)
    + [WakeOnLAN](https://github.com/Steffo99/spegnimi-bot)
    + [ShortURLsBot](https://github.com/MarcoBuster/ShortURLsBot)
* [DEPRECATED] Telepot - https://telepot.readthedocs.io/en/latest/

### C++
* [my cpp tutorials](./tutorials-cpp)
* C++ lib for Bot - https://github.com/reo7sp/tgbot-cpp
* Telegram Bot API - https://github.com/desmoteo/telegram-bot-api [DEPRECATED]

## Learning/Education
* Bots: An introduction for developers - https://core.telegram.org/bots
* Telegram Bot API - https://core.telegram.org/bots/api
* Sample examples -  https://core.telegram.org/bots/samples#python
* __THEORY__ - https://github.com/python-telegram-bot/python-telegram-bot/wiki
* How to create a Telegram Bot with Node.js - https://www.youtube.com/watch?v=Te7HcRhwOI4

## Github Repositories
* Bot with Google App Engine (GAP) - https://github.com/yukuku/telebot
* Collection great groups, channels, bots and libraries for Telegram - https://github.com/ebertti/awesome-telegram
* Collection of Bots - https://github.com/DenisIzmaylov/awesome-telegram-bots

## Bots
* Weather Bot using JS - https://www.3scale.net/2016/02/create-a-weather-bot-for-telegram/
* Bot with Amazon AWS cloud - https://lesterchan.net/blog/2016/03/11/telegram-bot-using-aws-api-gateway-and-aws-lambda/
* Bot with GAE - 
  - https://github.com/FollonSaxBass/python-telegram-bot-GAE
  - https://github.com/yukuku/telebot
  - https://github.com/livz/LizBot
* [Article by a Toptal Engineer](https://www.toptal.com/python/telegram-bot-tutorial-python)


## Tools
* Emoji
  - https://emojipedia.org/
  - https://apps.timwhitlock.info/emoji/tables/unicode
  - Or Google the required type with 'emoji' as suffix. E.g. "person standing emoji", "cow emoji", etc.
  - get bytes from unicode
    - M-1: Just copy the emoji & literally paste into unicode place [here](https://onlineunicodetools.com/convert-unicode-to-bytes)
    - M-2: Just copy the emoji & literally paste into the variable place inside the `.py` file
    - get the bytes & write like this:
```py
person_emoji = '👤'              # b'\xf0\x9f\x91\xa4'.decode('utf-8') U+1F464
purse_emoji = '👛'             # b'\xf0\x9f\x91\x9b'.decode('utf-8') U+1F519
```
  - usage
```py
itembtn0 = types.InlineKeyboardButton(f'{person_emoji} Account', callback_data = "home_account")
itembtn1 = types.InlineKeyboardButton(f'{purse_emoji} Wallet', callback_data = "home_wallet")
```

* ### TODO:
  - `Quiz Bot`
    + owner can add set of quiz Q&A
    + pay the subscription & make it available for users
  - `Birthday_bot`: reminds other users (in a group) about the Birthday boy/girl.
  - `Weather_bot`: gives alert about weather of a place (given by user).
  - `Stock_bot`: gives all stock market info
    + API: https://mboum.com/api/welcome
    + Features inspiration: https://mboum.com/
    + Earning: user subscription for 
      - specific price value alert for a share. E.g. alert when share price of Google reaches 1000 USD.
      - specific price of share daily e.g. Google, Uber, Amazon... 
