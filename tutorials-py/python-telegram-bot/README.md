# python-telegram-bot

## Background
* The Bot API is exposed via the telegram.Bot class. The methods are the snake_case equivalents of the methods described in the official Telegram Bot API. The exact camelCase method names as in the Telegram docs are also available for your convenience. So for example `telegram.Bot.send_message` is the same as `telegram.Bot.sendMessage`. All the classes of the Bot API can also be found in the `telegram` module, e.g. the `Message` class is available as `telegram.Message`.
* `getMe` is same as `get_me` and `sendMessage` to `send_message`.


## Tutorials
* [ ] Send message to the user
* [ ] Button callback query
* [ ] Read text message from the user
* [ ] Read photo message from the user


## Troubleshooting
* Note: The `use_context=True` is a special argument only needed for version 12 of the library. The default value is `False`. It allows for better backwards compatibility with older versions of the library, and to give users some time to upgrade. From version 13 `use_context=True` it is the default.
```py
from telegram.ext import Updater
updater = Updater(token='TOKEN', use_context=True)
```
* Telegram Bot Connection Error
```console
telegram.error.NetworkError: urllib3 HTTPError HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot1811588405:AAGwmuY793sviu2CTyJspqWY4XOVVg9hm8I/getMe (Caused by ConnectTimeoutError(<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x00000191FAD6EC40>, 'Connection to api.telegram.org timed out. (connect timeout=5.0)'))
```

	- __Problem__: This happens if there is some problem from your network blockage (mostly in Office).
	- __Solution__: Open the `request.py` in this location: "AppData\Local\Programs\Python\Python39\Lib\site-packages\telegram\utils\request.py" 
	- On line 140-150 you can find something like this
```
kwargs = dict(
    maxsize=con_pool_size,
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where(),
    socket_options=sockopts,
    timeout=urllib3.Timeout(connect=self._connect_timeout, read=read_timeout, total=None),
)
```
	- Do this and it will be worked: [NOTE: With warnings, but worked]
```
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
kwargs = dict(
    maxsize=con_pool_size,
    cert_reqs='CERT_NONE',
    ca_certs=certifi.where(),
    socket_options=sockopts,
    timeout=urllib3.Timeout(connect=self._connect_timeout, read=read_timeout, total=None),
)
```


## References
* [Github](https://github.com/python-telegram-bot/python-telegram-bot)
* [Documentation](https://python-telegram-bot.readthedocs.io/en/latest/index.html)
* [Github Wiki](https://github.com/python-telegram-bot/python-telegram-bot/wiki)