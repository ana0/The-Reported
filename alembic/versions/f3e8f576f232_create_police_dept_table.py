"""Create police dept table

Revision ID: f3e8f576f232
Revises: 867fe98c4032
Create Date: 2016-12-03 10:09:50.279798

"""
from alembic import op
import sqlalchemy as db

import os, sys
basedir = os.path.abspath(os.path.dirname(__file__))
dbpath = os.path.join(basedir, '..', '..')
print dbpath
sys.path.append(dbpath)

from app.models import provinces

# revision identifiers, used by Alembic.
revision = 'f3e8f576f232'
down_revision = '867fe98c4032'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('police_depts',
        db.Column('id', db.Integer, primary_key=True),
        db.Column('name', db.String(200), nullable=False),
        db.Column('city', db.String(100), nullable=False),
        db.Column('province', db.Enum(*[p for p in provinces], name='province'), 
            nullable=False),
        db.Column('investigating', db.String(100)),
    )
    op.add_column('incidents', db.Column('police_id', db.Integer, 
        db.ForeignKey('police_depts.id')))


def downgrade():
    op.drop_column('incidents', 'police_id')
    op.drop_table('police_depts')

