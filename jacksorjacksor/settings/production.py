from .base import *

DEBUG = False

ALLOWED_HOSTS = ['jacksorjacksor.eu.pythonanywhere.com']

ROOT_URLCONF = 'jacksorjacksor.urls'

try:
    from .local import *
except ImportError:
    pass
