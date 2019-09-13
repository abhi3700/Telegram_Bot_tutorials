## Deploy Bot to your Server
`Heroku` is the server used for Bot deployment.

## System
Windows 10

## Installation
* [Download and Install](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
* __Version__: `$ heroku --version`
* __Login__: `$ heroku login`
>	NOTE: a file - `_netrc` is created in the directory "C:\Users\abhijit". On Windows, the file is named `_netrc`
	
	Now, the heroku is logged in.

	[MORE](https://devcenter.heroku.com/articles/heroku-cli#getting-started)

## Runtime (specify python version)
* Define a specific version of python using `runtime.txt` in app’s root directory like this:
```txt
python-3.6.9
```
[MORE](https://devcenter.heroku.com/articles/python-runtimes)
> NOTE: The runtime.txt format is case-sensitive and must not include spaces. You must also specify all three version number components (major, minor, and patch) in runtime.txt.
> If you don’t follow this format, your app will fail to deploy.
* It is optional to create this, but you may get a message like this:
```console
remote:
remote: -----> Python app detected
remote:  !     Python has released a security update! Please consider upgrading to python-3.6.9
remote:        Learn More: https://devcenter.heroku.com/articles/python-runtimes
```
* New apps come with latest python version available in Heroku. For using specific version (say old), one can use this technique.

## App
* create a new App using Heroku dashboard [RECOMMENDED]. Or else, one can create App via CLI. Go to the last part in [this](https://devcenter.heroku.com/articles/heroku-cli#getting-started)
> NOTE: Keep the App name same as the repo (git, heroku)
* __Procfile__: Heroku apps include a Procfile that specifies the commands that are executed by the app on startup.
> Note:  `Procfile.txt` is not valid.
* Including a `requirements.txt` in the root directory is one way for Heroku to recognize your Python app.
```txt
botogram2
requests
```
* __Procedure__ (The bot's repo is maintained with git in Heroku server)
	- Ensure heroku is logged in in the CLI.
	- After creating app, copy the link `Heroku Git URL` from App's settings page.
	- Run `$ git remote add heroku <heroku-git-url>` from inside the Bot repo.
	- After commits, run `$ git push heroku master` to push the repo into the heroku server.

## Database
### Redis Database
* Add `Heroku Redis` as addon in an App. For more, click [here](https://devcenter.heroku.com/articles/heroku-redis)
* Check if a Redis instance is provisioned in your App. For more, click [here](https://devcenter.heroku.com/articles/heroku-redis#check-if-a-redis-instance-is-already-provisioned)
	- If installed in App:
		```console
		abhijit@Abhijit MINGW64 /i/heroku_repos/keyhubbot (master)
		$ heroku addons | grep heroku-redis
		heroku-redis (redis-aerodynamic-59195)  hobby-dev  free   created
		```
	- If not installed in App:
		```console
		abhijit@Abhijit MINGW64 /i/heroku_repos/leolabbot (master)
		$ heroku addons | grep heroku-redis		
		```
* Capture `REDIS_URL` by following this:
```console
abhijit@Abhijit MINGW64 /i/heroku_repos/keyhubbot (master)
$ heroku config | grep REDIS
REDIS_URL: redis://h:p478e373c898b3eb564e2a14303db09c415cfcacffa638404d3378e2ffb@ec2-3-222-131-127.compute-1.amazonaws.com:13819
```
* Implement in the code by following [here](https://devcenter.heroku.com/articles/heroku-redis#connecting-in-python)
	1. First install this package using `pip install redis`
```py
import os
import redis
REDIS_URL = "redis://h:p478e373c898b3eb564e2a14303db09c415cfcacffa638404d3378e2ffb@ec2-3-222-131-127.compute-1.amazonaws.com:13819"
r = redis.from_url(os.environ.get(REDIS_URL))
```

### Postgres Database
* Add `Heroku Postgres` as addon in an App. For more, click [here](https://devcenter.heroku.com/categories/heroku-postgres)
* Capture `DATABASE_URL` by following this:
```console
abhijit@DESKTOP-VEMB324 MINGW64 /i/heroku_repos/keyhubbot (master)
$ heroku config
=== keyhubbot Config Vars
DATABASE_URL: postgres://sncwwevyyzviez:7569a516be40f3f5d62f6d6a8818556771c5f1ade86096b96dabeb01bef14c37@ec2-54-247-96-169.eu-west-1.compute.amazonaws.com:5432/dm8m5ustplad3
REDIS_URL:    redis://h:pd4a2fa90f5a63058400930ffd21f5864312b2a174061846e13543a79eb1fdd81@ec2-54-77-8-133.eu-west-1.compute.amazonaws.com:18179
```

## Troubleshooting
* whenever the bot is deployed, and if doesn't work, then try to run `python app/bot.py` command on the heroku console in App's Home screen.
* For testing purpose, always use local PC via `heroku local` command. Actually, in Heroku one gets limited usage in FREE membership.