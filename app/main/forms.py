from flask_wtf import Form
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms import IntegerField, FloatField, DateField, validators

from ..models import genders_table, races_table, armed_table
from ..models import classifications_table, charges_table, provinces_table

def format_form_choices(table):
    """takes table, a dictionary, and formats the key/value pairs as a list of 
    tuples, which is the format required for SelectFields"""
    choice_data = []
    for key in table:
        choice_data.append((key, table[key]))
    return choice_data

class AddIncidentForm(Form):
    """This is going to be a very long form"""
    name = StringField('Full name:', 
        validators=[validators.required(message="A name is required"), 
        validators.length(
            message=("Name must be less than 100 characters"), max=100)])
    age = IntegerField('Age:', 
        validators=[validators.required(message=("Age is required"), 
        validators.numberrange(max=150, message=("Age must be less than 150"))])
    gender = SelectField('Gender:', choices=format_form_choices(genders_table), 
        validators=[validators.required(message="Gender is required")])
    race = SelectField('Race:', choices=format_form_choices(races_table), 
        validators=[validators.required(message="Race is required")])
    armed = SelectField('Was the deceased armed?', 
        choices=format_form_choices(armed_table), 
        validators=[validators.required(
            message="Marking whether the deceased was armed is required")])
    charges = SelectField('Status of charges:', 
        choices=format_form_choices(charges_table),
        validators=[validators.required(
            message="Status of charges is required")])
    classification = SelectField('How was the death classified?', 
        choices=format_form_choices(classifications_table),
        validators=[validators.required(
            message="Classification of the death is required")])
    alleged_suicide = BooleanField('Was the death an alleged suicide?', 
        validators=[validators.required(
            message=("Marking whether the death is an alleged suicide is "
                "required")])
    mental_health = BooleanField(('Was there an indication of mental health '
        'barriers or distress?'),
        validators=[validators.required(
            message=("Marking whether there was an indication of mental health"
                " barriers is required")])
    postal_code = StringField('Postal Code', validators=[validators.optional(),
        validators.length(max=6, 
            message="Postal Code must be less than 6 characters"))])
    latitude = FloatField('Latitude:', validators=[validators.optional()])
    longitude = FloatField('Longitude', validators=[validators.optional()])
    submitted_by = StringField('Submitted by:', 
        validators=[validators.optional(), validators.length(
            message=("Submitted by name must be less than 100 characters"), 
            max=100)])
    occured_date = DateField("Date of incident:", 
        validators=[validators.optional()])
    needs_review = BooleanField("Does this entry need review?", 
        validators=validators=[validators.optional()])


#add item to inventory form
# class AddInventoryItemForm(Form):
# 	designId = SelectField('Design Id:', validators=[validators.required()])
# 	piece = SelectField('Piece:', validators=[validators.required()])
# 	materialId = SelectField('Material:', validators=[validators.required()])
# 	inStudio = BooleanField('In studio?', validators=[validators.optional()])
# 	notes = StringField('Notes:', validators=[validators.optional()])

# class EditInventoryItemForm(Form):
# 	designId = SelectField('Design Id:', validators=[validators.required()])
# 	piece = SelectField('Piece:', validators=[validators.required()])
# 	materialId = SelectField('Material:', validators=[validators.required()])
# 	inStudio = BooleanField('In studio?', validators=[validators.optional()])
# 	notes = StringField('Notes:', validators=[validators.optional()])
# 	submit = SubmitField('Update')

# 	def __init__(self, itemid, *args, **kwargs):
# 		super(EditInventoryItemForm, self).__init__(*args, **kwargs)
# 		self.designId.choices = designs
# 		self.piece.choices = pieces
# 		self.materialId.choices = materials
# 		self.itemid = itemid
# 		# self.designId.default = itemid.design_id

# class DeleteConfirm(Form):
# 	submit = SubmitField('Delete it')
# 	itemid = StringField('Item id')

	# def __init__(self, itemid, *args, **kwargs):
	# super(DeleteConfirm, self).__init__(*args, **kwargs)
	# self.itemid = itemid