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