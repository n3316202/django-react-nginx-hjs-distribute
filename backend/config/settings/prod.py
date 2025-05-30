# config/settings/prod.py
# 배포환경
#pip install python-decouple

from .base import *
from decouple import config

# DEBUG = config('DEBUG', default=False, cast=bool)

# #SECRET_KEY = config('DJANGO_SECRET_KEY')

# ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS').split(',')

# CORS_ALLOWED_ORIGINS = [
#     config('CORS_ALLOWED_ORIGIN'),
# ]

# CSRF_TRUSTED_ORIGINS = [
#     config('CSRF_TRUSTED_ORIGIN'),
# ]

DEBUG = True
ALLOWED_HOSTS = ["*"]

#dev_6_2
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 정적파일 URL 경로
STATIC_URL = '/static/'

# collectstatic 명령어로 모이는 폴더 (EC2 내 정적파일 모음 경로)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# (개발 중에만) 추가 정적파일 경로 지정 가능
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Using Mysql

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'distribute',
        'USER': 'distribute',
        'PASSWORD': 'distribute',
        'HOST': 'db',
        'PORT': '3306',
    }
}