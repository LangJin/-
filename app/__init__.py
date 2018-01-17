# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()
def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    return app
