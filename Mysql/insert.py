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
    jane_doe_id=3
    new_date="2024-01-15"
    time=45
    progress=2
    def add_workout_session(member_id, date, duration_minutes, calories_burned):
        cursor=conn.cursor()
        query=" INSERT INTO members(member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
     
        cursor.execute(query,(jane_doe_id,new_date,time,progress))
       
        
        if conn and conn.is_connected():
            print(f" New session added for member {jane_doe_id}")
            pass
            cursor.close()
            conn.close()
    conn.commit()
except Error as e:
    print("There seems to be an error")
    
finally:
     print (f" New session added for member {jane_doe_id}") 
