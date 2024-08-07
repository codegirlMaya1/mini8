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
    update_age=("42",2)
    update_id=("5",2)
    
    #Assuming Bob Green has an id of 2
    def update_member_age(member_id, new_age):
        cursor=conn.cursor()
        query="UPDATE members SET age = %s WHERE %s"
        query1="UPDATE members SET id = %s WHERE %s"
        cursor.execute(query,update_age)
        cursor.execute(query1,update_id)
        
        if conn and conn.is_connected():
            print("Member data updated successfully")
            pass
            cursor.close()
            conn.close()
    conn.commit()
except Error as e:
    print("There seems to be an error")
    
finally:
     print (" Member data updated successfully") 