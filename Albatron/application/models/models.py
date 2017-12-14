# -*- coding:utf-8 -*-
'''
时间：2017-12-12
作者：Jin
说明：操作数据库的类
'''
from application import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


class Adminhux(db.Model):
    '''管理员表'''
    __tablename__ = 'h_admin'
    id = db.Column(db.Integer, primary_key=True)
    usercount = db.Column(db.String(64), unique=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64), unique=True)
    admin_photo = db.Column(db.String(128), default=None)
    email = db.Column(db.String(128), default=None)
    remark = db.Column(db.String(128), default=None)
