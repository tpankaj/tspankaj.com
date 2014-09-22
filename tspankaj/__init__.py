# Library imports
from datetime import datetime
from flask import *
from flask.ext.mongoengine import *
from flask.ext.login import LoginManager, login_required, current_user, login_user, logout_user
from flask.ext.bcrypt import Bcrypt

# Application setup
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'db': 'tspankaj'}
db = MongoEngine(app)
bcrypt = Bcrypt(app)

# Application imports
import tspankaj.models
import tspankaj.views

# Top-level context processors
@app.context_processor
def get_date():
    return dict(year=datetime.today().year)

@app.context_processor
def get_pages():
    #return dict(pages=[c.name for c in Category.objects])
    return dict()

# Top-level routes
@app.route('/robots.txt')
def robots_txt():
    return app.send_static_file('robots.txt')

@app.route('/humans.txt')
def humans_txt():
    return app.send_static_file('humans.txt')
