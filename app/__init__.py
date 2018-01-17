# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from .resources.admin import api_admin


db = SQLAlchemy()


def create_app(configname):
    app = Flask(__name__)
    app.config.from_object(config[configname])
    db.init_app(app)
    app.register_blueprint(api_admin)
    return app
