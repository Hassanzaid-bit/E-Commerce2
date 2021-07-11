from .base import *

DEBUG = True

DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.sqlite',
        'NAME' : os.path.join(BASE_DIR, 'db.sqlite3')
    }
}