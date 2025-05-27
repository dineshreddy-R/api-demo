import json
import psycopg2
from flask import Flask

app = Flask(__name__)
dine_db_host = "pg-12c7bdf1-reddy94.l.aivencloud.com"
db_name = "defaultdb"
user = "avnadmin"
pwd = "AVNS_Xtm8bKHSR1GtTelNyMC"
port = "15563"


@app.route("/")
def index_page():
    return "hello from index"

@app.route("/")
def dine():
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
    # Get column names
    colnames = [desc[0] for desc in cur.description]

    # Convert to list of dictionaries
    students = [dict(zip(colnames, row)) for row in result]
    cur.close()
    conn.close()
    return json.dumps(students)


if __name__ == "__main__":
    app.run(debug=True)
