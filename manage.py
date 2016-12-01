from app import create_app, db
from app.models import Inventory, Piece, Material, Design

app = create_app('default')

if __name__ == '__main__':
	app.run()