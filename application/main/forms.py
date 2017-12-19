# -*- coding:utf-8 -*-
'''
时间：2017-12-11
作者：浪晋
说明：各种客户端的表单
'''
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
