import psycopg2

dine_db_host = "pg-12c7bdf1-reddy94.l.aivencloud.com"
db_name = "defaultdb"
user = "avnadmin"
pwd = "AVNS_Xtm8bKHSR1GtTelNyMC"
port = "15563"

"""
DB related stuff
1. create connection
2. create cursor
3. run sql
4. close connection --> check in GPT
"""

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
    print('#'*6)
