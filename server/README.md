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

## Redis Database
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