# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_sqlalchemy import SQLAlchemy


#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or "sqlite:///db.sqlite"
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/users.sqlite"

db = SQLAlchemy(app)

from models import User




# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# send the jsonified results
@app.route("/login", methods=["GET", "POST"])
def login():
    
    if request.method == "POST":
        i_user = request.form["user-input"]
        i_password = request.form["password"]
  
        inputdata=[{"user" : i_user,
              "pwd" : i_password,
              }]

        x = User.query.filter_by(name=i_user).first()
        
        login = False
        
        if (x is None):
            user = User(name=i_user, pwd=i_password, status = True)
            db.session.add(user)
            db.session.commit()
            login = True
        else:
            if (x.pwd == i_password):
                if (x.status == False):
                    x.status = True 
                    db.session.commit()
                    login = True
             
    login_status ={"user" : i_user,
                   "login":login
                  }

   
    return jsonify(login_status)


@app.route("/user/<userID>/<userPwd>")
def user(userID, userPwd):
    
    
    x = User.query.filter_by(name=userID)
    
    login = False
    if (x.name == userID):
       if (x.pwd == userPwd):
            login = True
            
    done_ok ={'ok':ok}

    return render_template("index.html", done=done_ok)


@app.route("/deleteUser/<userID>")
def deleteUser(userID):
    
    x = User.query.filter_by(name=userID)
    
    db.session.delete(x)
    db.session.commit()        
            
    
    return render_template("index.html")


# should be deleted when go live - list all users in database:
@app.route("/list_users")
def list_users():
    
    results = db.session.query(User.name, User.pwd).all()

    users = []
    for result in results:
        users.append({
            "name": name[0],
            "pwd": pwd[1]
        })
    return jsonify(users)




if __name__ == "__main__":
    app.run()
