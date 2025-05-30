import psycopg2
import os
from dotenv import load_dotenv


from dine_db import dine_db_host, db_name, user, pwd, port

load_dotenv()


conn = psycopg2.connect(
    host=dine_db_host,
    dbname=db_name,
    user=user,
    password=pwd,
    port=port
)
print("connection created")
cur = conn.cursor()
sql = "insert into users(name,age,user_name,password) values (%s,%s,%s,%s)"
values=( 'hello', 20, 'hello', 'hello@123')
cur.execute(sql, values)
conn.commit()
cur.close()
conn.close()
print("values added sucessfully")
