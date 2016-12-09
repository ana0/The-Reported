"""Fix typo

Revision ID: d96996105058
Revises: 339fb1eb9450
Create Date: 2016-12-09 13:10:07.211710

"""
from alembic import op
import sqlalchemy as db

import os, sys
basedir = os.path.abspath(os.path.dirname(__file__))
dbpath = os.path.join(basedir, '..', '..')
print dbpath
sys.path.append(dbpath)

from app.models import classifications_table

# revision identifiers, used by Alembic.
revision = 'd96996105058'
down_revision = '339fb1eb9450'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('incidents', 'classication')
    op.add_column('incidents', db.Column('classification', 
        db.Enum(*[c for c in classifications_table], 
            name='classification'), nullable=False))



def downgrade():
    op.add_column('incidents', d.Column('classication', 
        db.Enum(*[c for c in classifications_table], 
            name='classification'), nullable=False))
    op.drop_column('incidents', 'classification')