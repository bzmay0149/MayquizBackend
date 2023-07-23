import mysql.connector

def create_connection():
    db_config = {
        'user': 'root',
        'password': 'admin',
        'host': '127.0.0.1',
        'database': 'mydb',
        'port': '3306'
    }
    connection = mysql.connector.connect(**db_config)
    return connection
   
