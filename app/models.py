from . import db

designs = [('cl', 'classics'), ('mj', 'momjeans')]
pieces = [('1', 'fronts'), ('2', 'left temple'), ('2', 'right temple'), ('3', 'finished frame')]
materials = [('bl', 'black'), ('ha', 'hacienda')]

#define models
class Piece(db.Model):
	__tablename__ = 'pieces'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	inventory = db.relationship('Inventory', backref='piece')

class Design(db.Model):
	__tablename__ = 'designs'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	inventory = db.relationship('Inventory', backref='design')

class Material(db.Model):
	__tablename__ = 'materials'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	inventory = db.relationship('Inventory', backref='material')

class Inventory(db.Model):
	__tablename__ = 'inventory'
	id = db.Column(db.Integer, primary_key=True)
	piece_id = db.Column(db.String, db.ForeignKey('pieces.name'))
	design_id = db.Column(db.Integer, db.ForeignKey('designs.id'))
	material_id = db.Column(db.Integer, db.ForeignKey('materials.id'))
	# piece_id = db.Column(db.String())
	# design_id = db.Column(db.String())
	# material_id = db.Column(db.String())
	in_studio = db.Column(db.Boolean)
	notes = db.Column(db.String())
