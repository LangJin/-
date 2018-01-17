# -*- coding:utf-8 -*-
from app import db
'''
假装是个数据库
'''
userinfo = [
    {"username": "jin", "password": "a123456"},
    {"username": "tony", "password": "a123456"},
    {"username": "tom", "password": "a123456"}
]


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64))

    @staticmethod
    def init_db():
        db.drop_all()
        db.create_all()

    @staticmethod
    def init_datas():
        user_a = User(username='Jin', password="a123456")
        user_b = User(username='Ben', password="a123456")
        user_c = User(username='Len', password="a123456")
        db.session.add_all([user_a, user_b, user_c])
        db.session.commit()
