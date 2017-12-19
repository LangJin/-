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

    @staticmethod
    def initrole():
        admin_role = Role(name='Admin')
        mod_role = Role(name='Moderator')
        user_role = Role(name='User')
        db.session.add(admin_role)
        db.session.add(mod_role)
        db.session.add(user_role)
        # db.session.add_all(
        #     [admin_role, mod_role, user_role])
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @staticmethod
    def inituser():
        user_john = User(username='john', role_id=1)
        user_susan = User(username='susan', role_id=1)
        user_david = User(username='david', role_id=3)
        db.session.add(user_john)
        db.session.add(user_susan)
        db.session.add(user_david)
        # db.session.add_all(
        #     [user_john, user_susan, user_david])
        db.session.commit()

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
