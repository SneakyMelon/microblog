"""
    # views.py
    Returns views as web pages back to the browser.
"""
from flask import render_template, flash, redirect
#from flask_login import login_required #, current_user
from app import app
from options import opt
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    """/index or home routing.
    Initial landing space for all users who are visiting the application.
    """
    return render_template('index.html', options=opt())

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    /login routing. Provides an interface for users to login in to the application.
    Redirects user to homepage if logged in, otherwise shows login form.

    :return: view login.html
    :redirect: /index.html
    """

    form = LoginForm()

    if form.validate_on_submit():
		# Get Form data by using the format:
		# 	form.<form_object_id>.data

        flash('Login Requested for OpenID_%s and Remember_token_%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index?logged_in')
    return render_template('login.html',
                           options=opt(),
                           form=form,
                           providers=app.config['PROVIDERS'])

#@app.route('/dashboard')
#@login_required
#def account():
    #"""
    #/account dashboard for users.

    #:return: view account.html
    #"""
    #return render_template("account.html")
