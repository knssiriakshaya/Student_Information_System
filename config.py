import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        port='3306',#enter your MySQL port number here 
        user='user_name',#enter your MySQL username here
        password='password',#enter your MySQL password here
        database='student_management'
    )
    return conn
