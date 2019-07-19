#from .app import db
from mahjong_app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    pwd = db.Column(db.String(20))
    status = db.Column(db.String(1))
                    

    def __repr__(self):
        return '<User %r>' % (self.name)
