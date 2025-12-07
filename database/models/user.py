from peewee import Model, CharField, DateTimeField
from database.database import db
import datetime

class lojas(Model):
    name = CharField()
    date = DateTimeField(default=datetime.datetime.now)
    email = CharField(unique=True)

    class Meta:
        database = db
