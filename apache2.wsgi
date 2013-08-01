#!/usr/bin/python 
import os
import sys
 
django_app='mysite'
#cpath=os.path.join( os.path.dirname(os.path.dirname(__file__) + '..', django_app)
cpath=os.path.dirname(__file__) 
#if os.path.islink(__file__):
#	cpath=os.path.join( os.path.dirname(__file__), os.path. )

if cpath not in sys.path:
    sys.path.insert(0,cpath )
 
os.environ['DJANGO_SETTINGS_MODULE'] = django_app+'.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
