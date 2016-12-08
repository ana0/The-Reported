"""Edit incident fields

Revision ID: 339fb1eb9450
Revises: f3e8f576f232
Create Date: 2016-12-08 11:20:33.600726

"""
from alembic import op
import sqlalchemy as db


# revision identifiers, used by Alembic.
revision = '339fb1eb9450'
down_revision = 'f3e8f576f232'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('details', 'description', existing_type=db.String(200),
        type_=db.String(2000))
    op.alter_column('details', 'media_source', existing_type=db.String(200),
        type_=db.String(300))
    op.alter_column('details', 'image_of', existing_type=db.String(200),
        type_=db.String(300))



def downgrade():
    op.alter_column('details', 'description', existing_type=db.String(2000),
        type_=db.String(200))
    op.alter_column('details', 'media_source', existing_type=db.String(300),
        type_=db.String(200))
    op.alter_column('details', 'image_of', existing_type=db.String(300),
        type_=db.String(200))


