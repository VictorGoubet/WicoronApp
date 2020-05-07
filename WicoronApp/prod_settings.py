from .settings import *
import dj_database_url

DEBUG = False
TEMPLATE_DEBUG=False

DATABASES['default']=dj_database_url.config()

ALLOWED_HOSTS = ['wicoronapp.herokuapp.com']

MIDDLEWARE+=['whitenoise.middleware.WhiteNoiseMiddleware',]



SECRET_KEY = os.environ['SECRET_KEY']