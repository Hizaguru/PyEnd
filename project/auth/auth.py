from crypt import methods
from requests import request, session
from .import auth
from project.database.db import connect_to_database, user_exist
from flask import render_template, request, redirect, url_for, session


# GET request   methods for authentication  with    MySQLdb backend backend.
@auth.route('/', methods=['GET', 'POST'])
def login():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        #Check if username and password POST request exists.
        username = request.form['username']
        password = request.form['password']
        print("hi")
        #Establish connection to the database.
        connection = connect_to_database()
        #Check if user and password exists.
        select_all_query = 'SELECT * FROM accounts WHERE username  = %s AND password = %s', (username, password)
        account = user_exist(connection, select_all_query, username, password)
        print(account)
        #if Account exists.
        if account is not None:
            print("J1")
            #Create session data.
            session['loggedin'] = True
            print('session is ', session['loggedin'])
            select_id_query = 'SELECT id FROM accounts WHERE username  = %s AND password = %s', (username, password)
            
            session['id'] = user_exist(connection, select_id_query, username, password)
            print('Session id', session['id'] )
            select_username_query = 'SELECT username FROM accounts WHERE username  = %s AND password = %s', (username, password)
            session['username'] = user_exist(connection, select_username_query, username, password)
            print('username', session['username'])
            #Redirect to login page
            return redirect('/upload')
        else:
            print("incorrect username & password")
            #Incorrect credentials, or account doesn't exist.
            msg = 'Please go home. There is nothing here to see'
            return redirect('/')
    #Render the login form with the message.
    return render_template('login.html', msg=msg)


@auth.route('/signup')
def signup():
    return 'Signup'


@auth.route('/register')
def register():
    return 'Register'


@auth.route('/logout')
def logout():
    return 'Logout'
