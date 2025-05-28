import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()

dine_db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
pwd = os.getenv("DB_PASSWORD")
port = os.getenv("DB_PORT")

conn = psycopg2.connect(
    host=dine_db_host,
    dbname=db_name,
    user=user,
    password=pwd,
    port=port
)

print("conncetion created")
cur = conn.cursor()
sql = ("select user_name,password from users where user_name = 'dine123' AND password = 'dine@123'")
cur.execute(sql)
result = cur.fetchall()
conn.close()

print (result)