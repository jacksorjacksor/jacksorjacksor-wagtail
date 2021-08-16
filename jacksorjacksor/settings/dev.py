from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-iq=90lh(-(!6r&h^$67g066_c#5n$u(s3@3x*gt^7*+21#^7pr'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['jacksorjacksor.eu.pythonanywhere.com', 'localhost', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
