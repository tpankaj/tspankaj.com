activate_this = '/var/www/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
from tspankaj import app as application
