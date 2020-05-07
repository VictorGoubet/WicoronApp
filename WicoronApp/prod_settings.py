from .settings import *
import dj_database_url

DEBUG = True
TEMPLATE_DEBUG=True

DATABASES['default']=dj_database_url.config()

ALLOWED_HOSTS = ['wicoronapp.herokuapp.com']

MIDDLEWARE+=['whitenoise.middleware.WhiteNoiseMiddleware',]

TEMPLATES=[{
    'APP_DIRS': True,
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ['templates'],
    'OPTIONS': {'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'social_django.context_processors.backends',
        'social_django.context_processors.login_redirect']}
        }]



SECRET_KEY = os.environ['SECRET_KEY']