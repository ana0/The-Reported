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
                    ('u', 'Unknown')]

provinces_table = [('PE', 'PEI'),
            ('ON', 'Ontario'),
            ('QC', 'Quebec'),
            ('AB', 'Alberta'),
            ('BC', 'British Columbia'),
            ('MB', 'Manitoba'),
            ('NB', 'New Brunswick'),
            ('NL', 'Newfoundland and Labrador'),
            ('NT', 'Northwest Territories'),
            ('NS', 'Nova Scotia'),
            ('NU', 'Nunavut'),
            ('SK', 'Saskatchewan'),
            ('YT', 'Yukon Territor')]

class Detail(models.Model):
    armed = models.TextField('Details about whether the deceased was armed', max_length=500, blank=True)
    charges = models.TextField('Details about the charges or conviction', max_length=500, blank=True)
    mental_health = models.TextField('Detailed mental health information', max_length=500, blank=True)
    classification = models.TextField('Details about the classification of the death', max_length=500, blank=True)
    media_source = models.URLField('Urls of media source', max_length=500, blank=True)
    image_of = models.URLField('Url of an image of the deceased', max_length=500, blank=True)
    address = models.CharField('Expanded address the event occured at', max_length=150, blank=True)
    description = models.TextField('Long form description of the event', max_length=3000, blank=True)

class PoliceDept(models.Model):
    name = models.CharField('Name', max_length=500, db_index=True)
    city = models.CharField('City, town, or jurisdiction', max_length=200, db_index=True)
    province = models.CharField('Province', 
        choices=provinces_table, 
        default='PE', 
        db_index=True,
        max_length=2)
    investigating = models.CharField('investigating body', max_length=500, db_index=True)

class Incident(models.Model):
    # __tablename__ = 'incidents'
    # id = db.Column(db.Integer, primary_key=True)
    name = models.CharField('Full Name', max_length=250, db_index=True)
    age = models.IntegerField('Age', db_index=True)
    gender = models.CharField('Gender', 
        choices=genders_table, 
        default='u', 
        db_index=True,
        max_length=1)
    race = models.CharField('Race/Ethnicity', 
        choices=races_table, 
        default='u', 
        db_index=True,
        max_length=2)
    armed = models.CharField('Was the deceased armed?', choices=armed_table, max_length=1,
        default='u', db_index=True)
    charges = models.CharField('Status of charges or conviction', 
        choices=charges_table, 
        default='u', 
        db_index=True,
        max_length=1)
    classification = models.CharField('Status of charges or conviction', 
        choices=classifications_table, 
        default='u', 
        db_index=True,
        max_length=1)
    alleged_suicide = models.BooleanField('Was the death an alleged suicide?', db_index=True)
    mental_health = models.BooleanField(('Was there an indication of mental '
        'health barriers or distress?'), db_index=True)
    postal_code = models.CharField('Postal Code', max_length=6, blank=True)
    latitude = models.FloatField('Latitude', blank=True, db_index=True)
    longitude = models.FloatField('Longitude', blank=True, db_index=True)
    submitted_by = models.CharField('Submitted by', max_length=150, blank=True)
    created_date = models.DateField('Submission date', auto_now_add=True)
    updated_date = models.DateField('Updated date', auto_now=True)
    occured_date = models.DateField('Occured date', db_index=True)
    needs_review = models.BooleanField('Needs Review', db_index=True)
    details = models.OneToOneField(Detail, on_delete=models.CASCADE, related_name='details_from')
    police = models.ForeignKey(PoliceDept, on_delete=models.CASCADE, db_index=True, related_name='police_dept_of')


