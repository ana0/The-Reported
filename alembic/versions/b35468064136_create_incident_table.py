"""Create incident table

Revision ID: b35468064136
Revises: 
Create Date: 2016-12-02 12:42:15.991643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b35468064136'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'incident',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.Unicode(100), nullable=False),
        sa.Column('gender', sa.String(1)),
        sa.Column('race', sa.String(2)),
        sa.Column('armed', sa.Boolean)
    )
    pass


def downgrade():
    pass
