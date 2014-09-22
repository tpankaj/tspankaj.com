from flask import *
from flask.ext.mongoengine import *

class Post(Document):
    title = StringField(required=True, unique=True)
    link = StringField(required=True, unique=True)
    body = StringField(required=True)
    publish_date = DateTimeField(required=True)
    published = BooleanField(required=True)
    author = ReferenceField(User, required=True, reverse_delete_rule=CASCADE)
    category = ReferenceField(Category, required=True)
    meta = {'allow_inheritance': True}

class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)

class Category(Document):
    name = StringField(required=True, unique=True)
    link = StringField(required=True, unique=True)
