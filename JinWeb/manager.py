# -*- coding:utf-8 -*-
'''
启动文件，在这里对整个项目进行启动，初始化等等
'''
from flask_script import Manager, Shell
from flask import render_template
from app.models import User
from app import create_app, db

app = create_app('default')


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager = Manager(app)
manager.add_command('shell', Shell(make_shell_context))


@manager.command
def init_db():
    db.drop_all()
    db.create_all()


@manager.command
def init_user():
    User.insert_values()


if __name__ == '__main__':
    manager.run()
