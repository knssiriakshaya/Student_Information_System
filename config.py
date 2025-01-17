import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='root',
        database='student_management'
    )
    return conn
