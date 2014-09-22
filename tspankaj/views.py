#from flask import *
#from flask.ext.mongoengine import *
from . import *

@app.route('/')
def index():
    return 'Hello, world!'
