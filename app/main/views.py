from flask import render_template, Flask, redirect, url_for, flash
from . import main
from .forms import AddIncidentForm
from .. import db
# from ..models import Inventory, Material, Design, Piece, designs, pieces, materials

@main.route('/')
def hello_world():
    return render_template('index.html')

# @app.route('/<name>/')
# def inventory_home(name="inventory"):
# 	return render_template('inventory_home.html', name="inventory")

@main.route('/add_inventory/', methods=("GET","POST"))
def inventory_home():
	pass
# 	form = AddInventoryItemForm()
# 	form.designId.choices = designs
# 	form.piece.choices = pieces
# 	form.materialId.choices = materials
# 	if form.validate_on_submit():
# 		flash('Item Added')
# 		item = Inventory(design_id=str(form.designId.data), piece_id=str(form.piece.data), material_id=str(form.materialId.data), in_studio=form.inStudio.data, notes=str(form.notes.data))
# 		db.session.add(item)
# 		db.session.commit()
# 		return redirect(url_for('.inventory_home'))
# 		# return str(form.designId.data)
# 	return render_template('inventory_home.html', form=form)

@main.route('/browse_inventory/', methods=("GET","POST"))
def inventory_browse():
	pass
# 	form = DeleteConfirm()
# 	inventory = Inventory.query.all()
# 	if form.validate_on_submit():
# 		flash('Item Deleted')
# 		item_to_delete = form.itemid.data
# 		item = Inventory.query.get(item_to_delete)
# 		db.session.delete(item)
# 		return redirect(url_for('.inventory_browse'))
# 	return render_template('inventory_browse.html', inventory=inventory, form=form)
# 	#return str(len(str(inventory[0])))
# 	#return "hello"

# @main.route('/edit_inventory/', methods=("GET","POST"))
# def inventory_test():
# 	return "cats"

# @main.route('/edit_inventory/<itemid>', methods=("GET","POST"))
# def inventory_edit(itemid):
# 	item = Inventory.query.get(itemid)
# 	design__id = item.design_id
# 	piece__id = item.piece_id
# 	material__id = item.material_id
# 	in__studio = item.in_studio
# 	notes__ = item.notes
# 	form = EditInventoryItemForm(itemid=item)
# 	if form.validate_on_submit():
# 		flash('Item Updated')
# 		item.design_id = form.designId.data
# 		item.piece_id = form.piece.data
# 		item.material_id = form.materialId.data
# 		item.in_studio = form.inStudio.data
# 		item.notes = form.notes.data
# 		db.session.add(item)
# 		db.session.commit()
# 		return redirect(url_for('.inventory_edit', itemid=item.id))
# 	form.designId.default = design__id
# 	form.piece.default = piece__id
# 	form.materialId.default = material__id
# 	form.inStudio.default = in__studio
# 	form.notes.default = notes__
# 	form.process()
# 	return render_template('inventory_edit.html', form=form)




