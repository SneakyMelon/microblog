"""
from flask import Flask
"""

from flask import Flask
from app import views

APP = Flask(__name__)
APP.config.from_object('config')
