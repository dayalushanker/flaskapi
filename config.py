import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Cor@1234@localhost/fapi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False