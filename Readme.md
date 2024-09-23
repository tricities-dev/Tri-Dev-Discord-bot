# Tri-Dev Discord Bot

This bot is a general utility tool designed to assist in managing, maintaining, and entertaining users on the Tri-Dev Discord server.

## Prerequisites

### Docker

Docker is used to create a local database for development purposes. It is recommended to continue using Docker throughout the development process to ensure consistency and troubleshoot common issues that may have been encountered and resolved before.

- [Download Docker Desktop](https://www.docker.com/products/docker-desktop)

### Python 3.10.12

This project requires Python 3.10.12. Installing a Python version manager like pyenv can help manage multiple Python versions on your machine.

- [Python Version Manager (pyenv)](https://github.com/pyenv/pyenv)

### Test Discord Server

Before deploying or merging changes, it’s essential to test the bot on a test Discord server. Creating a new server for testing is straightforward.

- [How to Create a Discord Server](https://support.discord.com/hc/en-us/articles/204849977-How-do-I-create-a-server)

### Discord Developer Account & Bot Token

To integrate the bot into Discord, you'll need a Discord Developer account and a bot token. Both are easy to obtain:

- [Create Developer Account](https://discord.com/developers/docs/intro)
- [Get Access Token](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token)

### Creating Proper Intents

You need to let Discord know what intents you are using. We currently only need the message_contents intent

- [Change Intent](https://discordpy.readthedocs.io/en/latest/intents.html)

### Freezing Dependencies (Important)

To ensure the project dependencies are consistent, freeze any new dependency installations into the `requirements.txt` file.

```bash
pip3 freeze > requirements.txt
```

## Running the Bot Locally

Use the Makefile to simplify setup and execution. Follow these steps to get started:

```bash
make initial-setup
make db-migrate
make run
```
