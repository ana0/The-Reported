from __future__ import unicode_literals

from django.db import models

# Create your models here.

genders_table = [('m', 'Male'),
                ('f', 'Female'),
                ('o', 'Other'),
                ('u', 'Unknown')]

races_table = [('i', 'Indigenous'),
                ('b', 'Black'),
                ('w', 'White'),
                ('wa', 'Arab/West Asian'),
                ('n', 'Asian'),
                ('sa', 'South Asian'),
                ('m', 'Mixed Race'),
                ('se', 'Southeast Asian'),
                ('l', 'Latin American'),
                ('o', 'Other'),
                ('u', 'Unknown')]

armed_table = [('y', 'Yes'),
        ('n', 'No'),
        ('u', 'Unknown')]

charges_table = [('n', 'No Charges'),
                ('l', 'Charges Laid'),
                ('c', 'Conviction'),
                ('i', 'Under Investigation'),
                ('u', 'Unknown')]

classifications_table = [('g', 'Gunshot'),
                    ('o', 'Other'),
                    ('c', 'CEW'),
                    ('u' 'Unknown')]

class Incidents(models.Model):
    # __tablename__ = 'incidents'
    # id = db.Column(db.Integer, primary_key=True)
    name = models.CharField('Full Name', max_length=150)
    age = models.IntegerField('Age')
    gender = models.CharField('Gender', choices=genders_table, default='u')
    race = models.CharField('Race/Ethnicity', choices=races_table, default='u')
    armed = models.CharField('Was the deceased armed?', choices=armed_table, 
        default='u')
    charges = models.CharField('Status of charges or conviction', 
        choices=charges_table, 
        default='u')
    classification = models.CharField('Status of charges or conviction', 
        choices=classifications_table, 
        default='u')
    alleged_suicide = models.BooleanField('Was the death an alleged suicide?')
    mental_health = models.BooleanField(('Was there an indication of mental '
        'health barriers or distress?'))
    postal_code = models.CharField('Postal Code', max_length=6, blank=True)
    latitude = models.FloatField('Latitude', blank=True)
    longitude = models.FloatField('Longitude', blank=True)
    submitted_by = models.CharField('Submitted by', max_length=150, blank=True)
    created_date = models.DateField('Submission date', auto_now_add=True)
    updated_date = models.DateField('Updated date', auto_now=True)
    occured_date = models.DateField('Occured date')
    needs_review = models.BooleanField('Needs Review')
    details = models.ForeignKey(Details, on_delete=models.CASCADE)
    police = models.ForeignKey(PoliceDepts, on_delete=models.CASCADE)

class Details(models.Model):
    armed = db.Column(db.String(200))
    charges = db.Column(db.String(200))
    mental_health = db.Column(db.String(200))
    classification = db.Column(db.String(200))
    media_source = db.Column(db.String(300))
    image_of = db.Column(db.String(300))
    address = db.Column(db.String(200))
    description = db.Column(db.String(2000))
    incident_ = db.relationship('Incidents', uselist=False, back_populates="details_")