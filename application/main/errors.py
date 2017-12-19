# -*- coding:utf-8 -*-
'''
时间：2017-12-11
作者：浪晋
说明：404，500的路由
'''
from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('/errors/404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('/errors/500.html'), 500
