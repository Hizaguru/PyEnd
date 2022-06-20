from flask import Flask, render_template, request, redirect, url_for, session, Blueprint
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from project.database.db import if_user_exists, connect_to_database

auth = Blueprint('auth', __name__)


@auth.route('/', methods=['GET', 'POST'])   # GET request   methods for authentication  with    MySQLdb backend backend.
def login():
    message = ''
    #Check if req.method is post, and uname and password exists.
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        connection = connect_to_database()
        account_exists = if_user_exists(connection, "test", "test")
        if account_exists:
            #create session data which can be accessed from routes
            session['loggedin '] = True
            session['id'] = account_exists['ID']
            session['usernames'] = account_exists['Username']
            #redirect to home page
            return redirect('/upload')
            
    
    #check if username and password exists in the database.
    
    return "hi"

@auth.route('/signup')
def signup():
    return 'Signup'


@auth.route('/logout')
def logout():
    return 'Logout'
