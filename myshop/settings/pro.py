from .base import *

DEBUG = False

ADMINS = (
    ('hassanzaid', 'hzaid.hz@gmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME' : 'computerphile',
        'USER' : 'computerphileuser',
        'PASSWORD' : 'password',
        

    }
}