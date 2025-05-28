import psycopg2
import os
from dotenv import load_dotenv
from sqlalchemy import values

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
sql = "insert into users(id,name,age,user_name,password) values (%s,%s,%s,%s,%s)"
values=(7, 'dummy', 20, 'host_5', 'host@123')
cur.execute(sql, values)
conn.commit()
cur.close()
conn.close()
print("values added sucessfully")
