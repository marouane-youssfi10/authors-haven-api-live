from .base import *
from .base import env


DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default="VoQE5G6ZQGRFR345NSQSDOL325cds23nZEC23412dfsdd43QSDF26NS2352", 
)


ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.0.1"]

# django-insecure-*=g)&&92^k7zze3m+^4d4e-us-l_98t*rg-b5oah$-ho$-n#+^