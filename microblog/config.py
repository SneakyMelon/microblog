"""
Application configuration.
"""

import os.path
from options import env

APP_NAME = 'app'

WTF_CSRF_ENABLED = True
SECRET_KEY = env('secret.key')

PROVIDERS = [
    {'name' : 'Google', 'url' : 'https://www.google.com/accounts/o8/id'},
    {'name' : 'Yahoo', 'url' : 'http://openid.yahoo.com'},
    {'name' : 'AOL', 'url' : 'http://openid.aol.com/<username>'},
    {'name' : 'Flickr', 'url' : 'http://www.flickr.com/<username>'},
    {'name' : 'MyOpenID', 'url' : 'https://myopenid.com'}
]

# Database Related Content
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# C:\Users\Allan\Desktop\Python\microblog\microblog

#SQLITE_PROTOCOL = 'sqlite:///'
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False
