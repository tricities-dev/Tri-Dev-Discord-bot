from peewee import *
import os

db_user = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')
db_name = os.getenv('POSTGRES_DB')
db_host = os.getenv('POSTGRES_HOST')
db_port = os.getenv('POSTGRES_PORT')

db = PostgresqlDatabase(
            db_name,
            user=db_user,
            password=postgres_password,
            host=db_host,
            port=db_port
        )

class DbHandle:
    def db_connect(self, db_name, db_user, postgres_password, db_host, db_port) -> PostgresqlDatabase:
        return PostgresqlDatabase(
            db_name,
            user=db_user,
            password=postgres_password,
            host=db_host,
            port=db_port
        )

    class User(Model):
        id = AutoField()
        discord_id = CharField()
        username = CharField()
        discriminator = CharField()
        class Meta:
            database = db

    def create_table(self):
        db.connect()
        db.create_tables([self.User])
        db.close()
