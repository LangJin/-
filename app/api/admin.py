# -*- coding:utf-8 -*-
from flask_restful import reqparse, abort, Resource
from app.models import db


class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()
        userinfo = db.userinfo
        for userdict in userinfo:
            if args["username"] == userdict["username"]:
                if args["password"] == userdict["password"]:
                    return userdict
                else:
                    abort(401, message="密码错误，请重新输入。")
            else:
                abort(401, message="用户名“{}”不存在".format(args["username"]))
