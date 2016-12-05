from . import db


#Look up tables used to constuct the enums 
genders_table = {'m': 'Male',
                'f': 'Female',
                'o': 'Other',
                'u': 'Unknown'}

races_table = {'a': 'Aboriginal',
                'b': 'Black',
                'w': 'White',
                'wa': 'Arab/West Asian',
                'n': 'Asian',
                'sa': 'South Asian',
                'm': 'Mixed Race',
                'se': 'Southeast Asian',
                'l': 'Latin American',
                'u': 'Unknown'}

armed_table = {'y': 'Yes',
        'n': 'No',
        'u': 'Unknown'}

charges_table = {'n': 'No Charges',
                'l': 'Charges Laid',
                'c': 'Conviction',
                'i': 'Under Investigation',
                'u': 'Unknown'}

classifications_table = {'g': 'Gunshot',
                    'o': 'Other',
                    'c': 'CEW',
                    'u': 'Unknown'}

provinces_table = {'PE': 'PEI',
            'ON': 'Ontario',
            'QC': 'Quebec',
            'AB': 'Alberta',
            'BC': 'British Columbia',
            'MB': 'Manitoba',
            'NB': 'New Brunswick',
            'NL': 'Newfoundland and Labrador',
            'NT': 'Northwest Territories',
            'NS': 'Nova Scotia',
            'NU': 'Nunavut',
            'SK': 'Saskatchewan',
            'YT': 'Yukon Territor'}

#ADD YEAR COLUMN??
#upgrade length of description in details
#upgrade length of url fields

#define models
class Incidents(db.Model):
    __tablename__ = 'incidents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(100), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.Enum(*[g for g in genders_table], name='gender'), 
        nullable=False)
    race = db.Column(db.Enum(*[r for r in races_table], name='race'), nullable=False)
    armed = db.Column(db.Enum(*[a for a in armed_table], name='armed'), 
        nullable=False)
    charges = db.Column(db.Enum(*[c for c in charges_table], 
        name='charges'), nullable=False)
    classication = db.Column(db.Enum(*[c for c in classifications_table], 
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
    details_id = db.Column(db.Integer, db.ForeignKey('details.id'))
    details = db.relationship('Details', backref='incidents')
    police_id = db.Column(db.Integer, db.ForeignKey('PoliceDepts.id'))
    police_depts = db.relationship('PoliceDepts', backref='incidents')

class Details(db.Model):
    __tablename__ = 'details'
    id = db.Column(db.Integer, primary_key=True)
    race = db.Column(db.String(200))
    armed = db.Column(db.String(200))
    charges = db.Column(db.String(200))
    mental_health = db.Column(db.String(200))
    classification = db.Column(db.String(200))
    media_source = db.Column(db.String(300))
    image_of = db.Column(db.String(300))
    address = db.Column(db.String(200))
    description = db.Column(db.String(2000))
    incident = db.relationship('Incidents', uselist=False, backref='details')
  
class PoliceDepts(db.Model):
    __tablename__ = 'police_depts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    province = db.Column(db.Enum(*[p for p in provinces_table], 
        name='province'), nullable=False)
    investigating = db.Column(db.String(100))
    incidents= db.relationship('Incidents', backref='incidents')
