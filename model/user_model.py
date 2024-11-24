import mysql.connector
from mysql.connector import Error

class user_model:
    def __init__(self):
        try:
            temp_data = {
                "host": "127.0.0.1",
                "port": 3306,
                "user": "root",
                "password": "root"
            }
            connection = mysql.connector.connect(**temp_data)
            if connection.is_connected():
                print("Successfully connected to the database")
        except Error as e:
            print(f"Error connecting to the database: {e}")
            connection = None
        

    def user_model_test(self):
        return "This is testing"

