from settings import *

DEBUG = True
INTERNAL_IPS = ['127.0.0.1']
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)