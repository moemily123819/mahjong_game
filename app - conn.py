# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import sqlite3
from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or "sqlite:///db.sqlite"
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/mahjong.db"

db = SQLAlchemy(app)
        
#from models import User
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    NAME = db.Column(db.String(20))
    PWD = db.Column(db.String(20))
    STATUS = db.Column(db.String(1))

    def __repr__(self):
        return '<User %r>' % (self.name)

 
# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")



# send the jsonified results
@app.route("/login", methods=["GET", "POST"])
def login():
    print("login")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row[0], row[1], row[2])
        arr_users.append(row[0])
        arr_pwd.append(row[1])
        arr_status.append(row[2])
                 
    lastrec = cur.lastrowid
    nextrec = lastrec+1            
    print('nextrec :', nextrec)
    print('request method', request.method)
    
    if request.method == "POST":
        existing_user = request.form["existing-user"]
        existing_pwd = request.form["existing-pwd"]
        new_user = request.form["new-user"]
        new_pwd = request.form["new-pwd"]
  
        print('input :', existing_user, existing_pwd, new_user, new_pwd)
                
        error = 0 
        login = False        
                
        if (existing_user == " "):
        # adding a new user and allow access right away
            if (new_user != " " and new_pwd != " "):
                if (new_user in users):
                    error = 4
                else:
                    sql= '''INSERT INTO users (ID,NAME,PWD,STATUS) VALUES (nextrec, new_user, new_pwd, "1")''' ;
                    print('insert sql :', sql)
                    cur = conn.cursor()
                    cur.execute(sql)
                    current_user = new_user
                    lastrec = cur.lastrowid
                    nextrec = lastrec+1
                    login = True
                    print('user created :', new_user, new_pwd, current_user)
            else:
                current_user = " "     
        else:
            if (existing_user in users):
                index = users.index(existing_user)    
                if (existing_pwd == pwd[index]):
                    if (status[index] == '1'):
                        error = 3
                    else:
                        sql= '''UPDATE users SET STATUS = "1" where NAME = existing_user''' ;
                        print('update sql :', sql)
                        current_user = existing_user
                        cur = conn.cursor()
                        cur.execute(sql)
                        print('user updated :', existing_user, current_user)
                        login = True
                else:
                    error = 1
            else:
                error = 2
                
        login_status = {"user" : current_user,
                        "login" : True,
                        "error" : error}
                
        return jsonify(login_status) 




if __name__ == "__main__":
    app.run()
#    conn.close()