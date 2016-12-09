"""Create incidenett table

Revision ID: defe4eaa4ce0
Revises: 
Create Date: 2016-12-02 18:13:25.993828

"""
from alembic import op
import sqlalchemy as db

import os, sys
basedir = os.path.abspath(os.path.dirname(__file__))
dbpath = os.path.join(basedir, '..', '..')
print dbpath
sys.path.append(dbpath)

from app.models import genders_table, races_table, armed_table
from app.models import charges_table, classifications_table

# revision identifiers, used by Alembic.
revision = 'defe4eaa4ce0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('incidents',
        db.Column('id', db.Integer, primary_key=True),
        db.Column('name', db.Unicode(100), nullable=False),
        db.Column('age', db.Integer),
        db.Column('gender', db.Enum(*[g for g in genders], name='gender'), 
            nullable=False),
        db.Column('race', db.Enum(*[r for r in races], name='race'), 
            nullable=False),
        db.Column('armed', db.Enum(*[a for a in armed], name='armed'), 
            nullable=False),
        db.Column('charges', db.Enum(*[c for c in charges], 
            name='charges'), nullable=False),
        db.Column('classification', db.Enum(*[c for c in classifications], 
            name='classification'), nullable=False),
        db.Column('alleged_suicide', db.Boolean, nullable=False),
        db.Column('mental_health', db.Boolean, nullable=False),
        db.Column('postal_code', db.String(6)),
        db.Column('latitude', db.Float),
        db.Column('longitude', db.Float),
        db.Column('submitted_by', db.Unicode(100)),
        db.Column('created_date', db.Date),
        db.Column('updated_date', db.Date),
        db.Column('occured_date', db.Date),
        db.Column('needs_review', db.Boolean, nullable=False)
    )


def downgrade():
    op.drop_table('incidents')
   
