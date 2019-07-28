## Deploy Bot to your Server
`Heroku` is the server here.

## System
Windows 10

## Installation
* [Download and Install](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
* Use `cmd` instead of `git-bash` as it is slow in fetching in Windows 10.
* Check version: `> heroku --version`
* Enter credentials:
```console
> heroku login -i
```
>	NOTE: a file - `_netrc` is created in the directory "C:\Users\abhijit". On Windows, the file is named `_netrc`
	
	Now, the heroku is logged in.

## App
* create a new App using Heroku dashboard.
* __Procfile__: Heroku apps include a Procfile that specifies the commands that are executed by the app on startup.
> Note:  `Procfile.txt` is not valid.
* Including a `requirements.txt` in the root directory is one way for Heroku to recognize your Python app.
```txt
botogram2
requests
```
* __Procedure__ (The bot's repo is maintained with git in Heroku server)
	- After creating app, copy the link `Heroku Git URL` from App's settings page.
	- Run `$ git remote add heroku <heroku-git-url>` from inside the Bot repo.
	- After commits, run `$ git push heroku master` to push the repo into the heroku server.