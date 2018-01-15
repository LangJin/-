# -*- coding:utf-8 -*-
from flask import Flask
from flask_restful import Api


api = Api()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    api.init_app(app)
    return app
