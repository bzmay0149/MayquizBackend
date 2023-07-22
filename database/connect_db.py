import mysql.connector


def create_connection():
   
    
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="admin",
            database="mydb",
            port="3306"
        )
        print("Conn established")
        return conn
   
