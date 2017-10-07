from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from options import opt



@app.route('/')
@app.route('/index')

def index(options = opt()):
	return render_template('index.html', options = options)

@app.route('/login', methods=['GET', 'POST'])

def login(options = opt()):
	form = LoginForm()

	if form.validate_on_submit():
		# Get Form data by using the format:
		# 	form.<form_object_id>.data

		flash('Login Requested for OpenID_%s and Remember_token_%s' % 
			(form.openid.data, str(form.remember_me.data)))
		return redirect('/index?logged_in')
	return render_template('login.html', 
							options = options,
							form = form,
							providers = app.config['PROVIDERS'])


