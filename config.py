import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = 'catsareveryadorableandilovethem'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev-data.sqlite')

config = {
	'default': DevelopmentConfig,
}