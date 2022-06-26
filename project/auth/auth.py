from flask import Blueprint
from .import auth


# GET request   methods for authentication  with    MySQLdb backend backend.
@auth.route('/')
def login():
    return "Login"


@auth.route('/signup')
def signup():
    return 'Signup'


@auth.route('/register')
def register():
    return 'Register'


@auth.route('/logout')
def logout():
    return 'Logout'
