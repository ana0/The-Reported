from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CsrfProtect

from config import config


bootstrap = Bootstrap()
db = SQLAlchemy()
crsf = CsrfProtect()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	bootstrap.init_app(app)
	db.init_app(app)
	crsf.init_app(app)

	#let flask know which instance of the app 'app' is
	with app.app_context():
		#db.drop_all()
		db.create_all()

	from main import main as main_blueprint
	app.register_blueprint(main_blueprint)


	return app