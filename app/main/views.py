from flask import render_template, Flask, redirect, url_for, flash
from flask import make_response
from . import main
from .forms import AddIncidentForm
from .. import db
from ..models import Incidents, Details, PoliceDepts
from datetime import date
import json

@main.route('/')
def hello_world():
    return render_template('index.html')

# @app.route('/<name>/')
# def inventory_home(name="inventory"):
# 	return render_template('inventory_home.html', name="inventory")

@main.route('/add_incident/', methods=("GET","POST"))
def add_incident():
    """Renders the add incident form, validates contents on submission, and 
    adds it to the database if successful"""
    form = AddIncidentForm()
    #contents of police dept and investigating org dropdown must be populated
    #dynamically from database 
    #unknown is added to the list and set as the default option
    all_depts = PoliceDepts.query.all()
    form.police_dept.choices = [(i.id, i.name) for i in all_depts]
    form.police_dept.choices = [('u', 'Unknown')] + form.police_dept.choices
    form.police_dept.default = 'u'
    all_investigating = [(i.id, i.investigating) for i in all_depts]
    form.investigating.choices = all_investigating 
    form.investigating.choices = [('u', 'Unknown')] + form.investigating.choices
    form.investigating.default = 'u'
    if form.validate_on_submit():
        #if the form is successfully validated, add the correct tables to the
        #database
        flash('Incident added', 'success')
        created = date.today()
        detail = Details(race=form.race_comment.data, 
            armed=form.armed_comment.data, charges=form.charges_comment.data,
            mental_health=form.mental_health_comment.data, 
            classification=form.classification_comment.data, 
            media_source=form.media_source.data, image_of=form.image_of.data,
            address=form.address.data, description=form.description.data)
        incident = Incidents(name=form.name.data, age=form.age.data, 
            gender=form.gender.data, race=form.race.data, armed=form.armed.data,
            charges=form.charges.data, classification=form.classification.data,
            alleged_suicide=form.alleged_suicide.data, 
            mental_health=form.mental_health.data, 
            postal_code=form.postal_code.data, latitude=form.latitude.data, 
            longitude=form.longitude.data, submitted_by=form.submitted_by.data,
            created_date=created, occured_date=form.occured_date.data, 
            needs_review=form.needs_review.data, details_id=detail.id)
        return redirect(url_for('.add_incident'))
    for field, errors in form.errors.iteritems():
        for err in errors:
            flash(err, 'error')
    return render_template('add_incident.html', form=form)

@main.route('/models/<int:police_id>/', methods=["GET"])
def get_police_depts(police_id):
    dept = PoliceDepts.query.get(police_id)
    data = {'name': dept.name,
            'city': dept.city,
            'province': dept.province,
            'investigating': dept.investigating}
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response


# @main.route('/add_inventory/', methods=("GET","POST"))
# def inventory_home():
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




