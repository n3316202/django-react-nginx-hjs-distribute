# config/settings/prod.py
# 배포환경
#pip install python-decouple

# from .base import *
# from decouple import config

# DEBUG = config('DEBUG', default=False, cast=bool)

# #SECRET_KEY = config('DJANGO_SECRET_KEY')

# ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS').split(',')

# CORS_ALLOWED_ORIGINS = [
#     config('CORS_ALLOWED_ORIGIN'),
# ]

# CSRF_TRUSTED_ORIGINS = [
#     config('CSRF_TRUSTED_ORIGIN'),
# ]

from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]


