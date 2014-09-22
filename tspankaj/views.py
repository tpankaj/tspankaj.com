from flask import *
#from flask.ext.mongoengine import *

@app.route('/')
def index():
    return 'Hello, world!'
