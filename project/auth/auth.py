from crypt import methods
from requests import request, session
from .import auth
from project.database.db import connect_to_database, user_exist
from flask import render_template, request, redirect, url_for, session


# GET request   methods for authentication  with    MySQLdb backend backend.
@auth.route('/', methods=['GET', 'POST'])
def login():
    message=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        #Check if username and password POST request exists.
        username = request.form['username']
        password = request.form['password']
        
        #Establish connection to the database.
        connection = connect_to_database
        #Check if user and password exists.
        account = user_exist(connection, username, password)
        if account:
            #Create session data.
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            #Redirect to login page
            return redirect('/upload')
        else:
            #Incorrect credentials, or account doesn't exist.
            message = 'Please go home. There is nothing here to see'
    #Render the login form with the message.
    return render_template('login.html', msg=message)


@auth.route('/signup')
def signup():
    return 'Signup'


@auth.route('/register')
def register():
    return 'Register'


@auth.route('/logout')
def logout():
    return 'Logout'
