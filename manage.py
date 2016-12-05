from app import create_app, db
from app.models import Incidents, Details

app = create_app('default')

if __name__ == '__main__':
	app.run()
