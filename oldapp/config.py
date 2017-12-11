# -*- coding:utf-8 -*-
class Config:
    DEBUG = True  # 激活debug模式
    CSRF_ENABLED = True  # 激活wtf
    SECRET_KEY = 'you-will-never-guess'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/testweb'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True



class DeploymentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/testweb'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


config = {
    "default":DevelopmentConfig,
    "deploy": DeploymentConfig
}
