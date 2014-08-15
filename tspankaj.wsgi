#!/usr/bin/python
import sys
sys.path.insert(0,"/var/www/tspankaj.com/")
activate_this = '/opt/python/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
from tspankaj import app as application
