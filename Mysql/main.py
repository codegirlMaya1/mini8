import mysql.connector
from mysql.connector import Error

db_name=" gym_db"
user="root"
password="S05071984"
host="localhost"
try:
    conn=mysql.connector.connect(
    database=db_name,
    user=user,
    password=password,
    host=host
    
)
    if conn.is_connected():
        print("MySQL database is connected successfully")
        
   
except ValueError as e:
    print(f'Error: {e}')
 
finally:
    if conn and conn.is_connected():
       
        print(" MySQL database is open...")
    