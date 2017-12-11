# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db


class User(db.Model):
    __tablename__ = 'h_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=False)

    @staticmethod
    def insert_values():
        values = {
            'admin': 'test@email.com',
            'ben': 'testben@123.com',
            'jin': 'testjin@test.com'
        }
        for key in values:
            value = User.query.filter_by(name=key).first()
            if value is None:
                value = User(name=key, email=values[key])
            db.session.add(value)
        db.session.commit()

    def __repr__(self):
        return '<User %r>' % self.name
