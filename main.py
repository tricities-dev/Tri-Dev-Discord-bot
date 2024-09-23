# This example requires the 'message_content' intent.

import discord
import os
import sys
from dotenv import load_dotenv
from orm import db_handle




def env_details():
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    print(token)
    db_user = os.getenv('POSTGRES_USER')
    postgres_password = os.getenv('POSTGRES_PASSWORD')
    db_name = os.getenv('POSTGRES_DB')
    db_host = os.getenv('POSTGRES_HOST')
    db_port = os.getenv('POSTGRES_PORT')
    issues = [token, db_user, postgres_password, db_name, db_host, db_port]
    for issue in issues:
        if issue == None:
            print(f"Missing environment variable: {issue}")
            raise Exception(f"Missing environment variable")
    return token

def parse_system_args(system_args: list[str]):
    for i in system_args:
        if i == '--help':
            print('Usage: python main.py --token <token> --db_user <db_user> --postgres_password <postgres_password> --db_name <db_name> --db_host <db_host> --db_port <db_port>')
            sys.exit()
        if i == '--setup':
            print('Setting up database')
            env_details()
            db = db_handle.DbHandle()
            db.create_table()
            print('setup Complete')
            sys.exit()
    return


class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

def main():
    parse_system_args(sys.argv)
    token = env_details()
    print(token)
    intents = discord.Intents.default()
    intents.message_content = True
    postgress_db = db_handle.DbHandle()
    client = MyClient(intents=intents)
    client.run(token)

if __name__ == '__main__':
    main()