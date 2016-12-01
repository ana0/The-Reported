from flask import render_template, Flask, redirect, url_for
import sqlite3 as sql
import requests
import os

from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import Form, CsrfProtect
from wtforms import StringField, SelectField, BooleanField
from wtforms import validators

#set up app and csrf security features
app = Flask(__name__)
app.secret_key = 'myverylongsecretkey'
CsrfProtect(app)

#set up Bootstrap
Bootstrap(app)

#set up Database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

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
	piece_id = db.Column(db.Integer, db.ForeignKey('pieces.id'))
	design_id = db.Column(db.Integer, db.ForeignKey('designs.id'))
	material_id = db.Column(db.Integer, db.ForeignKey('materials.id'))
	in_studio = db.Column(db.Boolean)
	notes = db.Column(db.String())

#set up connection to the guild api
s = requests.Session()
url = "http://api.guildeyewear.ca/"
s.auth = ('wouldntyou', 'liketoknow')

#set up and connect to database
# try:
# 	db = sql.connect(db_name)

# 	cur = db.cursor()

# 	cur.execute("DROP TABLE IF EXISTS Main")
# 	cur.execute("DROP TABLE IF EXISTS Inventory")
# 	cur.execute("CREATE TABLE Main(Id INT, DesignId TEXT, Firstname TEXT, Familyname TEXT, Companyname TEXT, Templesmaterial TEXT, Frontsmaterial TEXT)")
# 	cur.execute("CREATE TABLE Inventory(DesignId TEXT, Piece INT, Material TEXT, Notes TEXT)")
# except sql.Error, e:
# 	print "Error %s:" % e.args[0]
# finally:
# 	if db:
# 		db.close()



#connect to api
# try:
	# r = s.get("http://api.guildeyewear.ca/orders.json")
	# f = r.json()
# except:
	#add something useful here
	# pass



#data structure to hold design id #'s and name strings
designs = []

#add item to inventory form
class AddInventoryItemForm(Form):
	designId = SelectField('Design Id:', choices=[('cl', 'classics'), ('mj', 'momjeans')], validators=[validators.required()])
	piece = SelectField('Piece:', choices=[('1', 'fronts'), ('2', 'left temple'), ('2', 'right temple'), ('3', 'finished frame')], validators=[validators.required()])
	materialId = SelectField('Material:', choices=[('bl', 'black'), ('ha', 'hacienda')], validators=[validators.required()])
	inStudio = BooleanField('In studio?', validators=[validators.optional()])
	notes = StringField('Notes:', validators=[validators.optional()])

#class to manipulate inventory item data
class InventoryItem:
	def __init__(self, designId, piece, materialId, notes):
		self.d = designId
		self.p = piece
		self.m = materialId
		self.n = notes

	def get_designId(self):
		return self.d

	def get_piece(self):
		return self.p

	def get_materialId(self):
		return self.m

	def get_notes(self):
		return self.n



@app.route('/')
def hello_world():
    return render_template('index.html')

# @app.route('/<name>/')
# def inventory_home(name="inventory"):
# 	return render_template('inventory_home.html', name="inventory")

@app.route('/add_inventory/', methods=("GET","POST"))
def inventory_home():
	form = AddInventoryItemForm()
	if form.validate_on_submit():
		item = Inventory(design_id=form.designId.data, piece_id=form.piece.data, material_id=form.materialId.data, in_studio=form.inStudio.data, notes=form.notes.data)
		db.session.add(item)

		# 	return redirect(url_for('inventory_home'))

		return "it worked"
	return render_template('inventory_home.html', form=form)

@app.route('/browse_inventory/')
def inventory_browse():
	pass


if __name__ == '__main__':
    app.run(debug=True)