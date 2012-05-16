from settings import *

#Django toolbar && django extensions
DEBUG = True
INTERNAL_IPS = ['127.0.0.1']
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
DEBUG_TOOLBAR_CONFIG = { 'INTERCEPT_REDIRECTS': False }
INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)
