# Botogram2

## Installation
* M-1: using pip [Windows, Linux]
	- `pip install botogram2` [Source](https://pypi.org/project/botogram2/)
* M-2: from source code [Windows, Linux]
```
$ git clone https://github.com/python-botogram/botogram.git
$ cd botogram
$ python setup.py install
```

<details>
<summary><b>View in CMD console: </b></summary>

```
$ python setup.py install
running install
running bdist_egg
running egg_info
creating botogram2.egg-info
writing botogram2.egg-info\PKG-INFO
writing dependency_links to botogram2.egg-info\dependency_links.txt
writing requirements to botogram2.egg-info\requires.txt
writing top-level names to botogram2.egg-info\top_level.txt
writing manifest file 'botogram2.egg-info\SOURCES.txt'
reading manifest file 'botogram2.egg-info\SOURCES.txt'
reading manifest template 'MANIFEST.in'
warning: no files found matching 'Makefile'
warning: no files found matching '*.mo' under directory 'botogram\i18n'
writing manifest file 'botogram2.egg-info\SOURCES.txt'
installing library code to build\bdist.win-amd64\egg
running install_lib
running build_py
creating build
creating build\lib
creating build\lib\botogram
copying botogram\api.py -> build\lib\botogram
copying botogram\bot.py -> build\lib\botogram
copying botogram\callbacks.py -> build\lib\botogram
copying botogram\commands.py -> build\lib\botogram
copying botogram\components.py -> build\lib\botogram
copying botogram\context.py -> build\lib\botogram
copying botogram\converters.py -> build\lib\botogram
copying botogram\crypto.py -> build\lib\botogram
copying botogram\decorators.py -> build\lib\botogram
copying botogram\defaults.py -> build\lib\botogram
copying botogram\exceptions.py -> build\lib\botogram
copying botogram\frozenbot.py -> build\lib\botogram
copying botogram\hooks.py -> build\lib\botogram
copying botogram\inline.py -> build\lib\botogram
copying botogram\messages.py -> build\lib\botogram
copying botogram\shared.py -> build\lib\botogram
copying botogram\syntaxes.py -> build\lib\botogram
copying botogram\tasks.py -> build\lib\botogram
copying botogram\updates.py -> build\lib\botogram
copying botogram\__init__.py -> build\lib\botogram
creating build\lib\botogram\objects
copying botogram\objects\base.py -> build\lib\botogram\objects
copying botogram\objects\callbacks.py -> build\lib\botogram\objects
copying botogram\objects\chats.py -> build\lib\botogram\objects
copying botogram\objects\inline.py -> build\lib\botogram\objects
copying botogram\objects\markup.py -> build\lib\botogram\objects
copying botogram\objects\media.py -> build\lib\botogram\objects
copying botogram\objects\messages.py -> build\lib\botogram\objects
copying botogram\objects\mixins.py -> build\lib\botogram\objects
copying botogram\objects\polls.py -> build\lib\botogram\objects
copying botogram\objects\updates.py -> build\lib\botogram\objects
copying botogram\objects\__init__.py -> build\lib\botogram\objects
creating build\lib\botogram\runner
copying botogram\runner\ipc.py -> build\lib\botogram\runner
copying botogram\runner\jobs.py -> build\lib\botogram\runner
copying botogram\runner\processes.py -> build\lib\botogram\runner
copying botogram\runner\shared.py -> build\lib\botogram\runner
copying botogram\runner\__init__.py -> build\lib\botogram\runner
creating build\lib\botogram\utils
copying botogram\utils\calls.py -> build\lib\botogram\utils
copying botogram\utils\deprecations.py -> build\lib\botogram\utils
copying botogram\utils\startup.py -> build\lib\botogram\utils
copying botogram\utils\strings.py -> build\lib\botogram\utils
copying botogram\utils\__init__.py -> build\lib\botogram\utils
creating build\bdist.win-amd64
creating build\bdist.win-amd64\egg
creating build\bdist.win-amd64\egg\botogram
copying build\lib\botogram\api.py -> build\bdist.win-amd64\egg\botogram
copying build\lib\botogram\bot.py -> build\bdist.win-amd64\egg\botogram
copying build\lib\botogram\callbacks.py -> build\bdist.win-amd64\egg\botogram
copying build\lib\botogram\commands.py -> build\bdist.win-amd64\egg\botogram
copying build\lib\botogram\components.py -> build\bdist.win-amd64\egg\botogram
copying build\lib\botogram\context.py -> build\bdist.win-amd64\egg\botogram
copying build\lib\botogram\converters.py -> build\bdist.win-amd64\egg\botogram
copying build\lib\botogram\crypto.py -> build\bdist.win-amd64\egg\botogram
copying build\lib\botogram\decorators.py -> build\bdist.win-amd64\egg\botogram
copying build\lib\botogram\defaults.py -> build\bdist.win-amd64\egg\botogram
copying build\lib\botogram\exceptions.py -> build\bdist.win-amd64\egg\botogram
copying build\lib\botogram\frozenbot.py -> build\bdist.win-amd64\egg\botogram
copying build\lib\botogram\hooks.py -> build\bdist.win-amd64\egg\botogram
copying build\lib\botogram\inline.py -> build\bdist.win-amd64\egg\botogram
copying build\lib\botogram\messages.py -> build\bdist.win-amd64\egg\botogram
creating build\bdist.win-amd64\egg\botogram\objects
copying build\lib\botogram\objects\base.py -> build\bdist.win-amd64\egg\botogram\objects
copying build\lib\botogram\objects\callbacks.py -> build\bdist.win-amd64\egg\botogram\objects
copying build\lib\botogram\objects\chats.py -> build\bdist.win-amd64\egg\botogram\objects
copying build\lib\botogram\objects\inline.py -> build\bdist.win-amd64\egg\botogram\objects
copying build\lib\botogram\objects\markup.py -> build\bdist.win-amd64\egg\botogram\objects
copying build\lib\botogram\objects\media.py -> build\bdist.win-amd64\egg\botogram\objects
copying build\lib\botogram\objects\messages.py -> build\bdist.win-amd64\egg\botogram\objects
copying build\lib\botogram\objects\mixins.py -> build\bdist.win-amd64\egg\botogram\objects
copying build\lib\botogram\objects\polls.py -> build\bdist.win-amd64\egg\botogram\objects
copying build\lib\botogram\objects\updates.py -> build\bdist.win-amd64\egg\botogram\objects
copying build\lib\botogram\objects\__init__.py -> build\bdist.win-amd64\egg\botogram\objects
creating build\bdist.win-amd64\egg\botogram\runner
copying build\lib\botogram\runner\ipc.py -> build\bdist.win-amd64\egg\botogram\runner
copying build\lib\botogram\runner\jobs.py -> build\bdist.win-amd64\egg\botogram\runner
copying build\lib\botogram\runner\processes.py -> build\bdist.win-amd64\egg\botogram\runner
copying build\lib\botogram\runner\shared.py -> build\bdist.win-amd64\egg\botogram\runner
copying build\lib\botogram\runner\__init__.py -> build\bdist.win-amd64\egg\botogram\runner
copying build\lib\botogram\shared.py -> build\bdist.win-amd64\egg\botogram
copying build\lib\botogram\syntaxes.py -> build\bdist.win-amd64\egg\botogram
copying build\lib\botogram\tasks.py -> build\bdist.win-amd64\egg\botogram
copying build\lib\botogram\updates.py -> build\bdist.win-amd64\egg\botogram
creating build\bdist.win-amd64\egg\botogram\utils
copying build\lib\botogram\utils\calls.py -> build\bdist.win-amd64\egg\botogram\utils
copying build\lib\botogram\utils\deprecations.py -> build\bdist.win-amd64\egg\botogram\utils
copying build\lib\botogram\utils\startup.py -> build\bdist.win-amd64\egg\botogram\utils
copying build\lib\botogram\utils\strings.py -> build\bdist.win-amd64\egg\botogram\utils
copying build\lib\botogram\utils\__init__.py -> build\bdist.win-amd64\egg\botogram\utils
copying build\lib\botogram\__init__.py -> build\bdist.win-amd64\egg\botogram
byte-compiling build\bdist.win-amd64\egg\botogram\api.py to api.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\bot.py to bot.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\callbacks.py to callbacks.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\commands.py to commands.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\components.py to components.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\context.py to context.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\converters.py to converters.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\crypto.py to crypto.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\decorators.py to decorators.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\defaults.py to defaults.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\exceptions.py to exceptions.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\frozenbot.py to frozenbot.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\hooks.py to hooks.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\inline.py to inline.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\messages.py to messages.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\objects\base.py to base.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\objects\callbacks.py to callbacks.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\objects\chats.py to chats.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\objects\inline.py to inline.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\objects\markup.py to markup.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\objects\media.py to media.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\objects\messages.py to messages.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\objects\mixins.py to mixins.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\objects\polls.py to polls.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\objects\updates.py to updates.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\objects\__init__.py to __init__.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\runner\ipc.py to ipc.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\runner\jobs.py to jobs.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\runner\processes.py to processes.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\runner\shared.py to shared.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\runner\__init__.py to __init__.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\shared.py to shared.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\syntaxes.py to syntaxes.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\tasks.py to tasks.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\updates.py to updates.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\utils\calls.py to calls.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\utils\deprecations.py to deprecations.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\utils\startup.py to startup.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\utils\strings.py to strings.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\utils\__init__.py to __init__.cpython-37.pyc
byte-compiling build\bdist.win-amd64\egg\botogram\__init__.py to __init__.cpython-37.pyc
creating build\bdist.win-amd64\egg\EGG-INFO
copying botogram2.egg-info\PKG-INFO -> build\bdist.win-amd64\egg\EGG-INFO
copying botogram2.egg-info\SOURCES.txt -> build\bdist.win-amd64\egg\EGG-INFO
copying botogram2.egg-info\dependency_links.txt -> build\bdist.win-amd64\egg\EGG-INFO
copying botogram2.egg-info\not-zip-safe -> build\bdist.win-amd64\egg\EGG-INFO
copying botogram2.egg-info\requires.txt -> build\bdist.win-amd64\egg\EGG-INFO
copying botogram2.egg-info\top_level.txt -> build\bdist.win-amd64\egg\EGG-INFO
creating dist
creating 'dist\botogram2-0.6.1-py3.7.egg' and adding 'build\bdist.win-amd64\egg' to it
removing 'build\bdist.win-amd64\egg' (and everything under it)
Processing botogram2-0.6.1-py3.7.egg
creating c:\users\abhijit\anaconda3\lib\site-packages\botogram2-0.6.1-py3.7.egg
Extracting botogram2-0.6.1-py3.7.egg to c:\users\abhijit\anaconda3\lib\site-packages
Adding botogram2 0.6.1 to easy-install.pth file

Installed c:\users\abhijit\anaconda3\lib\site-packages\botogram2-0.6.1-py3.7.egg
Processing dependencies for botogram2==0.6.1
Searching for typing
Reading https://pypi.org/simple/typing/
Downloading https://files.pythonhosted.org/packages/05/d9/6eebe19d46bd05360c9a9aae822e67a80f9242aabbfc58b641b9
57546607/typing-3.7.4.3.tar.gz#sha256=1187fb9c82fd670d10aa07bbb6cfcfe4bdda42d6fab8d5134f04e8c4d0b71cc9
Best match: typing 3.7.4.3
Processing typing-3.7.4.3.tar.gz
Writing C:\Users\abhijit\AppData\Local\Temp\easy_install-xl5htnwq\typing-3.7.4.3\setup.cfg
Running typing-3.7.4.3\setup.py -q bdist_egg --dist-dir C:\Users\abhijit\AppData\Local\Temp\easy_install-xl5ht
nwq\typing-3.7.4.3\egg-dist-tmp-3gbfeyqo
zip_safe flag not set; analyzing archive contents...
Copying typing-3.7.4.3-py3.7.egg to c:\users\abhijit\anaconda3\lib\site-packages
Adding typing 3.7.4.3 to easy-install.pth file

Installed c:\users\abhijit\anaconda3\lib\site-packages\typing-3.7.4.3-py3.7.egg
Searching for requests==2.21.0
Best match: requests 2.21.0
Adding requests 2.21.0 to easy-install.pth file

Using c:\users\abhijit\anaconda3\lib\site-packages
Searching for Logbook==1.5.3
Best match: Logbook 1.5.3
Adding Logbook 1.5.3 to easy-install.pth file

Using c:\users\abhijit\anaconda3\lib\site-packages
Searching for chardet==3.0.4
Best match: chardet 3.0.4
Adding chardet 3.0.4 to easy-install.pth file
Installing chardetect-script.py script to C:\Users\abhijit\Anaconda3\Scripts
Installing chardetect.exe script to C:\Users\abhijit\Anaconda3\Scripts

Using c:\users\abhijit\anaconda3\lib\site-packages
Searching for certifi==2019.3.9
Best match: certifi 2019.3.9
Adding certifi 2019.3.9 to easy-install.pth file

Using c:\users\abhijit\anaconda3\lib\site-packages
Searching for urllib3==1.24.1
Best match: urllib3 1.24.1
Adding urllib3 1.24.1 to easy-install.pth file

Using c:\users\abhijit\anaconda3\lib\site-packages
Searching for idna==2.8
Best match: idna 2.8
Adding idna 2.8 to easy-install.pth file

Using c:\users\abhijit\anaconda3\lib\site-packages
Finished processing dependencies for botogram2==0.6.1

```

</details>

## Testing
* Successfully tested
```console
$ python bot.py
19:47.02 -   INFO    - Your bot is now running!
19:47.02 -   INFO    - Press Ctrl+C to exit.
19:51.04 -   INFO    - Shutting down the runner...
```
* With error
```console
$ python bot.py
Traceback (most recent call last):
  File "bot.py", line 23, in <module>
    @bot.command("deposit")
  File "C:\Users\abhijit\Anaconda3\lib\site-packages\botogram\bot.py", line 195, in __
    order=order, _from_main=True)
  File "C:\Users\abhijit\Anaconda3\lib\site-packages\botogram\components.py", line 126, in add_command
    raise NameError("The command /%s already exists" % name)
NameError: The command /deposit already exists
```