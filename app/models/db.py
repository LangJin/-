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


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), nullable=False, server_default='', unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False, unique=True, server_default='', index=True)
    role_id = db.Column(db.Integer, nullable=False, server_default='0')

    def __repr__(self):
        return '<User %r,Role id %r>' % (self.username, self.role_id)
