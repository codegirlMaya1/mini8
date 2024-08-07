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
    def new_member(id, name, age):
        cursor=conn.cursor()
        new_member=("5", "Sally Smith", "6")
        query=" INSERT INTO members(id, name, age) VALUES (%s, %s, %s)"
        cursor.execute(query,new_member)
        conn.commit()
        ab1=cursor
        print("New member added successfully")
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
except Error as e:
    
    print("There seems to be an error")
finally:
     print ("Connection now closed. Thank you")