import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
from dine_db import dine_db_host,db_name,user,pwd,port

conn = psycopg2.connect(
    host= dine_db_host,
    dbname=db_name,
    user=user,
    password=pwd,
    port=port
)
print("connection created")
cur=conn.cursor()
sql="update users set password= %s where user_name=%s"
values =('dine@222','dine123')
cur.execute(sql,values)
conn.commit()
cur.close()
conn.close()
print("updated sucessfully")
