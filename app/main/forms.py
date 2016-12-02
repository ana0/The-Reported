from flask_wtf import Form
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms import validators

# from ..models import designs, pieces, materials

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