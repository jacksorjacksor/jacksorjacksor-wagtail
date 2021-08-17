from .base import *

DEBUG = False

ALLOWED_HOSTS = ['jacksorjacksor.eu.pythonanywhere.com']

ROOT_URLCONF = 'jacksorjacksor.urls'

SECRET_KEY = '%+2&g)dpydd(^m)@t#2vynm)wce-es4*mapas#^uj1-w464+'

try:
    from .local import *
except ImportError:
    pass
