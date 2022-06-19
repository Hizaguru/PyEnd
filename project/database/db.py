from mysql.connector import Error
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def connect_to_database():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=os.getenv('HOST'),
            user=os.getenv('DATABASE_USER'),
            passwd=os.getenv('DATABASE_PASSWORD'),
            database=os.getenv('DATABASE_NAME')
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


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
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


def insert_image(name, photo, caption, size):
    print("Inserting BLOB into the table")
    try:
        connection = mysql.connector.connect(host=os.getenv('HOST'),
                                             database=os.getenv('DATABASE_NAME'),
                                             user=os.getenv('DATABASE_USER'),
                                             password=os.getenv('DATABASE_PASSWORD'))

        cursor = connection.cursor()
        sql_query = """ INSERT INTO Image
                          (Filename, Photo, Caption, FileSize) VALUES (%s,%s,%s,%s)"""

        image = convert_to_binary(photo)
        print(image)

        # Convert data into tuple format
        insert_blob_tuple = (name, image, caption, size)
        result = cursor.execute(sql_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


