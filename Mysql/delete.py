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
    member_id=1
    
    def delete_workout_session(session_id):
        if member_id ==1:
            cursor=conn.cursor()
            query="DELETE FROM workoutsessions WHERE id = %s"
        
        cursor.execute(query,member_id)
        
        if conn and conn.is_connected():
            print(f"Member #{member_id} deleted successfully")
            pass
            cursor.close()
            conn.close()
    conn.commit()
except Error as e:
    print("Member was not deleted")
    
finally:
     print (f"Member #{member_id} deleted successfully") 