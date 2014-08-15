#!/usr/bin/python
import sys
sys.path.insert(0,"/var/www/tspankaj.com/")
activate_this = '/opt/python/tspankaj.com/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import runserver
