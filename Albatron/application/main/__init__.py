# -*- coding:utf-8 -*-
'''
时间：2017-12-11
作者：浪晋
说明：注册蓝本
'''
from flask import Blueprint
from . import views, errors
main = Blueprint('main', __name__)
