import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

dine_db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
user = os.getenv("DB_USER")
pwd = os.getenv("DB_PASSWORD")
port = os.getenv("DB_PORT")

print(dine_db_host, db_name, user)
"""
DB related stuff
1. create connection
2. create cursor
3. run sql
4. close connection --> check in GPT
"""


if '__name__' == '__main__':
    conn = psycopg2.connect(
        host=dine_db_host,
        dbname=db_name,
        user=user,
        password=pwd,
        port=port
    )
    print("connection created")
    cur = conn.cursor()

    sql = "select * from student"
    cur.execute(sql)
    result = cur.fetchall()
    conn.close()

    for i in result:
        print(i)
        print('#' * 6)
