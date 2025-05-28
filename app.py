import json
import os

import psycopg2
from flask import Flask, render_template

app = Flask(__name__)
dine_db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
pwd = os.getenv("DB_PASSWORD")
port = os.getenv("DB_PORT")

@app.route("/login")
def login_page():
    # username paswd check here
    return render_template("login.html")


@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/api/students")
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
