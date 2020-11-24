"""Create manufacturers table

Revision ID: 75e879230a07
Revises: 
Create Date: 2020-11-24 13:13:44.858186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75e879230a07'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'manufacturers',
        sa.Column('manufacturer_id', sa.Integer, primary_key=True),
        sa.Column('manufacturer_name', sa.String(45), nullable=False),
        sa.Column('manufacturer_phone_nr', sa.String(45), nullable=True),
        sa.Column('manufacturer_address', sa.String(100), nullable=False)
    )


def downgrade():
    op.drop_table('manufacturers')