# -*- coding:utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from models import db
'''
是个数据库模型
'''


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    # password = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('密码不能读取！')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

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
