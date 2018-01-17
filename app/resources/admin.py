# -*- coding:utf-8 -*-
from flask_restful import reqparse, abort, Resource
from app.models.model import User
from flask import Blueprint
from flask_restful import Api


api_admin = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_admin)


class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()
        user = User.query.filter_by(username=args["username"]).first()
        if user is not None and user.verify_password(args["password"]):
            return "登陆成功"
        else:
            abort(401, message="用户名“{}”不存在,或者密码错误！".format(args["username"]))


api.add_resource(Login, '/login')
