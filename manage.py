from app import create_app, db
from app.models import Incident, Details

app = create_app('default')

if __name__ == '__main__':
	app.run()

#env.py
# import os, sys

# basedir = os.path.abspath(os.path.dirname(__file__))
# dbpath = os.path.join(basedir, '..')
# sys.path.append(dbpath)

# from app import db

# # app = create_app('default')
# target_metadata = db.metadata

#alembic.ini 
# sqlalchemy.url = sqlite:///%(here)s/dev-data.sqlite

# script_location = %(here)s/alembic