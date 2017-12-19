# -*- coding:utf-8 -*-
'''
时间：2017-12-11
作者：浪晋
说明：程序的路由保存在views中而错误处理程序保存在 app/main/errors.py 模块中。
导入这两个模块就能把路由和错误处理程序与蓝本关联起来。
注意，这些模块在 app/main/__init__.py 脚本的末尾导入，
这是为了避免循环导入依赖，
因为在views.py 和 errors.py中还要导入蓝本main,
模块中的蓝本需要在app/init下注册.
'''
from flask import Blueprint
main = Blueprint('main', __name__)
from . import errors
from . import views
