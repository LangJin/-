# -*- coding:utf-8 -*-
'''
时间：2017-12-11
作者：浪晋
说明：客户端的视图、路由
'''
from flask import session, url_for, render_template, redirect
from datetime import datetime
from ..models.models import User
from .. import db
from . import main
from .forms import NameForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template(
        '/client/index.html',
        form=form,
        name=session.get('name'),
        current_time=datetime.utcnow(),
        known=session.get('known', False))


@main.route('/user/<name>')
def user(name):
    return render_template('/client/user.html', name=name)
