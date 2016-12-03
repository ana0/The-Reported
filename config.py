import os
from secrets import password

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'catsareveryadorableandilovethem'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ('postgresql://localhost/thereported?user=ana0&' 
        'password=' + password)

config = {
    'default': DevelopmentConfig,
}