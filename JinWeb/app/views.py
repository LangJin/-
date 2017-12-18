# -*- coding:utf-8 -*-
from flask import render_template
from flask import Blueprint
hviews = Blueprint('hviews', __name__)


@hviews.app_errorhandler(404)
def page_not_found(e):
    return render_template('/errors/404.html'), 404


@hviews.app_errorhandler(500)
def internal_server_error(e):
    return render_template('/errors/500.html'), 500


@hviews.route('/', methods=['GET', 'POST'])
def index():
    return '<h1>Hello World!!!</h1>'
