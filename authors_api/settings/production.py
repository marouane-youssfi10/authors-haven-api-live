from .base import *
from .base import env

DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL",
    default="Authors Haven Support <ifssouy@gmail.com>",
)