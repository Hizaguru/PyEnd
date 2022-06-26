from flask import Blueprint
from project.database.db import if_user_exists, connect_to_database

auth = Blueprint('auth', __name__)


@auth.route('/')   # GET request   methods for authentication  with    MySQLdb backend backend.
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