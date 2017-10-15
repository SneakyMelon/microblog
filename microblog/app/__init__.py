"""
from flask import Flask
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Application related content
app = Flask(__name__)
app.debug = True
app.config.from_object('config')

# Database related content
db = SQLAlchemy(app)

from app import views, models
