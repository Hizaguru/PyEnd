import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv




load_dotenv()
host = os.getenv('HOST')
database = os.getenv('DATABASE_NAME')
user = os.getenv('DATABASE_USER')
password = os.getenv('DATABASE_PASSWORD')

def connect_to_database(hostname, username, password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            passwd=password,
            database=database
        )
        print("Connection to MYSQL DB Successful")
    except Error as e:
        print(f"Error {e} has occurred")

    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e} occurred.")

def db_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e} occurred")


def convert_to_binary(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binary_data = file.read()
    return binary_data






# create_image_table_query = """
# CREATE TABLE Image(
# Id INT NOT NULL AUTO_INCREMENT,
# Filename varchar(255),
# Photo mediumblob,
# Caption varchar(255),
# PRIMARY KEY (ID)
# )"""
# connection = connect_to_database(host, user, password, database)
# db_query(connection, create_image_table_query)
# create_db_query = "CREATE DATABASE picture"
# create_database(connection, create_db_query)

