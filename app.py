from flask import Flask
app=Flask(__name__)



@app.route('/')
def dine():
    return"this is flask"


if __name__=='__main__':
    app.run()