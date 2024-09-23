# Tri-Dev Discord bot

This is a general utility bot created to help manage/maintain and entertain users of the Tr-Dev discord.

## Pre-requisites

#### Docker

This project uses docker to create a local DB and it is recomended during development to keep in that tradition to make sure that any problems you may run into have already been addressed.

[Docker Desktop](https://www.docker.com/products/docker-desktop/)

#### Python 3.10.12

We use Python 3.10.12 in this project. Make sure to install it. Installing a python version manager is a great option to keep multiple versions of python available to you.

[Python Version Manager](https://github.com/pyenv/pyenv)

### A Test Discord Server

You want to be sure that you have a test in. Discord makes it's really easy to create a new server. This is where you can test your bot and changes before you make a merge request.

[Discord Server Creation](https://support.discord.com/hc/en-us/articles/204849977-How-do-I-create-a-server)

### Discord Developer account & Bot token

To actually interface with your bot you'll need a deeloper account & access token for your bot. Both are easy to obtain.

[Create Dev account](https://discord.com/developers/docs/intro)

[Get Access Token](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token)

### !Important freeze new dependncie isntalls

pip3 freeze > requirements.txt

## Run Locally
