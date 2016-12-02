from . import db

genders = {'m': 'Male',
                'f': 'Female',
                'o': 'Other',
                'u': 'Unknown'}

races = {'a': 'Aboriginal',
                'b': 'Black',
                'w': 'White',
                'wa': 'Arab/West Asian',
                'n': 'Asian',
                'sa': 'South Asian',
                'm': 'Mixed Race',
                'se': 'Southeast Asian',
                'l': 'Latin American',
                'u': 'Unknown'}

armed = {'y': 'Yes',
        'n': 'No',
        'u': 'Unknown'}

charges = {'n': 'No Charges',
                'l': 'Charges Laid',
                'c': 'Conviction',
                'i': 'Under Investigation',
                'u': 'Unknown'}

classifications = {'g': 'Gunshot',
                    'o': 'Other',
                    'c': 'CEW',
                    'u': 'Unknown'}



#define models
class Incident(db.Model):
    __tablename__ = 'incident'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(100), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.Enum(*[g for g in genders], name='gender'), 
        nullable=False)
    race = db.Column(db.Enum(*[r for r in races], name='race'), nullable=False)
    armed = db.Column(db.Enum(*[a for a in armed], name='armed'), 
        nullable=False)
    charges = db.Column(db.Enum(*[c for c in charges], 
        name='charges'), nullable=False)
    classication = db.Column(db.Enum(*[c for c in classifications], 
        name='classification'), nullable=False)
    alleged_suicide = db.Column(db.Boolean, nullable=False)
    mental_health = db.Column(db.Boolean, nullable=False)
    postal_code = db.Column(db.String(6))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    submitted_by = db.Column(db.Unicode(100))
    created_date = db.Column(db.Date)
    updated_date = db.Column(db.Date)
    occured_date = db.Column(db.Date)
    needs_review = db.Column(db.Boolean, nullable=False)


# class Design(db.Model):
#   __tablename__ = 'designs'
#   id = db.Column(db.Integer, primary_key=True)
#   name = db.Column(db.String(64))
#   inventory = db.relationship('Inventory', backref='design')

# class Material(db.Model):
#   __tablename__ = 'materials'
#   id = db.Column(db.Integer, primary_key=True)
#   name = db.Column(db.String(64))
#   inventory = db.relationship('Inventory', backref='material')

# class Inventory(db.Model):
#   __tablename__ = 'inventory'
#   id = db.Column(db.Integer, primary_key=True)
#   piece_id = db.Column(db.String, db.ForeignKey('pieces.name'))
#   design_id = db.Column(db.Integer, db.ForeignKey('designs.id'))
#   material_id = db.Column(db.Integer, db.ForeignKey('materials.id'))
#   # piece_id = db.Column(db.String())
#   # design_id = db.Column(db.String())
#   # material_id = db.Column(db.String())
#   in_studio = db.Column(db.Boolean)
#   notes = db.Column(db.String())
