"""
Django settings for my_microservice_project project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from .base import *
INSTALLED_APPS += ['users',]

ENABLED_APPS = [
    'users',           # The users app itself
]