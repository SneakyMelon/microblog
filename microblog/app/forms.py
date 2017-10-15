"""
Forms used throughout the application.
"""

from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    """
    Form found within the /login web page.

        :Form: stringField openid,
        :Form: BooleanField remember_me
    """
    openid = StringField('openid',
                         validators=[DataRequired('[Error_014]: This field data is required.')])
    remember_me = BooleanField('remember_me', default=False)
