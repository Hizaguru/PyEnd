from crypt import methods
from flask import render_template
from .import auth


# GET request   methods for authentication  with    MySQLdb backend backend.
@auth.route('/', methods=['GET', 'POST'])
def login():
    msg=''
    return render_template('login.html', msg='')


@auth.route('/signup')
def signup():
    return 'Signup'


@auth.route('/register')
def register():
    return 'Register'


@auth.route('/logout')
def logout():
    return 'Logout'
