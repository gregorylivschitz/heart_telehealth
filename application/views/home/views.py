from flask import render_template
from flask_login import login_required

from . import home

URL_list = ['ABOUT', 'SUNDAY', 'FIND', 'CONTACT']


@home.route('/')
@home.route('/index.html')
def index():
    return render_template('home/index.html', URL_list=URL_list)


@home.route('/dashboard')
@login_required
def dashboard():
    return render_template('home/dashboard.html')
