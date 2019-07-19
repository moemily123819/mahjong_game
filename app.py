# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import sqlite3
#from flask_socketio import SocketIO, join_room, emit
from flask_sqlalchemy import SQLAlchemy



#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#socketio = SocketIO(app)

#ROOMS = {} # dict to track active rooms




#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or "sqlite:///db.sqlite"
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
##app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/mahjong.db"

##db = SQLAlchemy(app)
        
#from models import User

#conn = sqlite3.connect("db/mahjong.db")
#print('conn', conn)


 
# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")



# send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
    print("send", request.method)
    arr_users=[]
    arr_pwd=[]
    arr_status = []
     
    if request.method == "POST":
        existing_user = request.form["existing-user"]
        existing_pwd = request.form["existing-pwd"]
        new_user = request.form["new-user"]
        new_pwd = request.form["new-pwd"]
        print('user entered :', new_user, new_pwd, existing_user, existing_pwd)
        input_info ={"existing_user" : existing_user,
                     "existing_pwd" : existing_pwd,
                     "new_user" : new_user,
                     "new_pwd" : new_pwd}
        conn = sqlite3.connect("db/mahjong.db")
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
        error = 0 
        login = False        
                
        if existing_user:
            print('existing user is NOT blank')
            if (existing_user in arr_users):
                current_user = existing_user
                index = arr_users.index(existing_user)    
                if (existing_pwd == arr_pwd[index]):
                    if (arr_status[index] == '1'):
                        error = 3
                        current_user = existing_user
                        login = False
                    else:
                        sql= '''UPDATE users SET STATUS = "1" where NAME = existing_user''' ;
                        print('update sql :', sql)
                        cur = conn.cursor()
                        cur.execute(sql)
                        conn.commit()
                        print('user updated :', existing_user, current_user)
                        login = True
                        login_status = {"user" : current_user,
                                        "login" : login,
                                        "error" : error}
                else:
                    login = False
                    error = 1
            else:
                error = 2
                current_user = " "
                login = False

        else:
            print('existing user is blank')
            # adding a new user and allow access right away
            if (new_user is not None and new_pwd is not None):
                if (new_user in arr_users):
                    error = 4
                else:
                    sql= '''INSERT INTO users (ID,NAME,PWD,STATUS) VALUES (nextrec, new_user, new_pwd, "1")''' ;
                    print('insert sql :', sql)
                    cur = conn.cursor()
                    cur.execute(sql)
                    current_user = new_user
                    nextrec = nextrec+1
                    conn.commit()
                    login = True
                    print('user created :', new_user, new_pwd, current_user)
                    login_status = {"user" : current_user,
                                    "login" : login,
                                    "error" : error}
                    
            else:
                current_user = new_user
                login = False
                error= 5
             
        login_status = {"user" : current_user,
                        "login" : login,
                        "error" : error}
                
        
        return redirect("/", code=302)
    
    
    return render_template("user_input.html")

    
    
    
    
@app.route("/login", methods=["GET", "POST"])
def login():

    conn = sqlite3.connect("db/mahjong.db")
    print('conn', conn)

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
    
    if request.method == "POST":
        print('GET')
        existing_user = request.form["existing-user"]
        print('existing-user', existing_user)
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
    
        return render_template("input_user.html")


#@socketio.on('create')

#def on_create(data):

#    """Create a game lobby"""

#    gm = game.Info(

#        size=data['size'],

#        teams=data['teams'],

#        dictionary=data['dictionary'])

#    room = gm.game_id

#    ROOMS[room] = gm

#    join_room(room)

#    emit('join_room', {'room': room})



if __name__ == "__main__":
    app.run()
#   socketio.run(app, debug=True)
