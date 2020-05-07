from .settings import *
import dj_database_url

DEBUG = False

DATABASES['default']=dj_database_url.config()

ALLOWED_HOSTS = ['wicoronapp.herokuapp.com']

MIDDLEWARE+=['whitenoise.middleware.WhiteNoiseMiddleware',]
TEMPLATE_DEBUG=True
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


SECRET_KEY = os.environ['SECRET_KEY']