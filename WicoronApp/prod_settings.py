from .settings import *
import dj_database_url

DEBUG = False

DATABASES['default']=dj_database_url.config()

ALLOWED_HOSTS = ['wicoronapp.herokuapp.com']

MIDDLEWARE+=['whitenoise.middleware.WhiteNoiseMiddleware',]
TEMPLATE_DEBUG=True
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


SECRET_KEY = 'j5)ti68(p_j30u$dtl0bm6xbhn0vkzi^q05--ejf*97vu)$fe1'