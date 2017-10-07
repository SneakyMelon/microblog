"""
Application configuration.
"""

from options import env

WTF_CSRF_ENABLED = True
SECRET_KEY = env('secret.key')

PROVIDERS = [
    {'name' : 'Google', 'url' : 'https://www.google.com/accounts/o8/id'},
    {'name' : 'Yahoo', 'url' : 'http://openid.yahoo.com'},
    {'name' : 'AOL', 'url' : 'http://openid.aol.com/<username>'},
    {'name' : 'Flickr', 'url' : 'http://www.flickr.com/<username>'},
    {'name' : 'MyOpenID', 'url' : 'https://myopenid.com'}
]
