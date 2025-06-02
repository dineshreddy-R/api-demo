import json
import os
from dotenv import load_dotenv
import psycopg2

from flask import Flask, render_template, request

from dine_db import dine_db_host

load_dotenv()

app = Flask(__name__)
dine_db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
pwd = os.getenv("DB_PASSWORD")
port = os.getenv("DB_PORT")


@app.route("/login", methods=['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['passx']
        conn = psycopg2.connect(
            host=dine_db_host,
            dbname=db_name,
            user=user,
            password=pwd,
            port=port
        )

        print("conncetion created")
        cur = conn.cursor()
        sql = f"select user_name,password from users where user_name ='{username}' AND password ='{password}'"
        print(sql)
        print('#' * 120)
        cur.execute(sql)
        result = cur.fetchall()
        conn.close()
        if result:
            return f"{username} {password}"
        else:
            print('Invalid username or password')
            return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/register",methods=['post','GET'])
def register_page():
    if request.method =='POST':
        #name= request.form['name']
        mail = request.form['mail']
        user_name = request.form['user_name']
        password = request.form['password']
        print(f"Data received: {user_name},{mail}, {password}")


        conn = psycopg2.connect(
            host=dine_db_host,
            dbname=db_name,
            user=user,
            password=pwd,
            port=port
        )
        print("connection created")
        cur = conn.cursor()
        sql = "insert into users(user_name,mail,password) values (%s,%s,%s)"
        values = ( user_name,mail,password)
        print('$'*20)
        cur.execute(sql, values)
        conn.commit()
        cur.close()
        conn.close()
        if values:
            return f"{user_name} Register sucessfull "
        else:
            print("invalied details")
            return render_template("register.html")
    else:
        return render_template("register.html")


@app.route("/")
def home_page():
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
