from sqlite3 import Cursor
import mysql.connector
from mysql.connector import errorcode
from unittest import TestCase
from mock import patch
import utils

MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_DB = "testdb"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"

class MockDb(TestCase):
    @classmethod
    def setUpclass(cls):
        cnx = mysql.connector.connect(
            host = MYSQL_HOST,
            user = MYSQL_USER,
            password = MYSQL_PASSWORD,
            port = MYSQL_PORT
        )

        cursor = cnx.cursor(dictionary=True)

            
        
        
