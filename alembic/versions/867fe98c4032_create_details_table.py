"""Create details table

Revision ID: 867fe98c4032
Revises: defe4eaa4ce0
Create Date: 2016-12-02 18:43:41.716212

"""
from alembic import op
import sqlalchemy as db


# revision identifiers, used by Alembic.
revision = '867fe98c4032'
down_revision = 'defe4eaa4ce0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('details',
        db.Column('id', db.Integer, primary_key=True),
        db.Column('race', db.String(200)),
        db.Column('armed', db.String(200)),
        db.Column('charges', db.String(200)),
        db.Column('classication', db.String(200)),
        db.Column('mental_health', db.String(200)),
        db.Column('media_source', db.String(200)),
        db.Column('image_of', db.String(200)),
        db.Column('address', db.String(200)),
        db.Column('description', db.String(200)),
    )
    op.add_column('incidents', db.Column('details_id', db.Integer, 
        db.ForeignKey('details.id')))

def downgrade():
    op.drop_column('incidents', 'details_id')
    op.drop_table('details')