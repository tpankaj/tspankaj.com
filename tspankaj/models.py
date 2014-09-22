from flask import *
from flask.ext.mongoengine import *
from . import db

class Post(db.Document):
    title = db.StringField(required=True, unique=True)
    link = db.StringField(required=True, unique=True)
    body = db.StringField(required=True)
    publish_date = db.DateTimeField(required=True)
    published = db.BooleanField(required=True)
    author = db.ReferenceField('User', required=True, reverse_delete_rule=CASCADE)
    category = ReferenceField('Category', required=True)

class Category(db.Document):
    name = db.StringField(required=True, unique=True)
    link = db.StringField(required=True, unique=True)

class User(db.Document):
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %s>' % self.username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.username)
