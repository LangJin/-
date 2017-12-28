# -*- coding:utf-8 -*-
'''
时间：2017-12-12
作者：浪晋
说明：启动整个项目的入口文件
'''
from application import create_app
app = create_app('default')


if __name__ == '__main__':
    app.run()
