"""create table stores

Revision ID: 96f9536c7d9c
Revises: 4add503fdd14
Create Date: 2020-11-17 15:07:12.677478

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '96f9536c7d9c'
down_revision = '4add503fdd14'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'stores',
        sa.Column('store_id', sa.Integer, primary_key=True),
        sa.Column('store_name', sa.String(45), nullable=False),
        sa.Column('store_phone_nr', sa.String(45), nullable=False),
        sa.Column('store_email', sa.String(45), nullable=False),
        sa.Column('store_address', sa.String(45), nullable=False)
    )


def downgrade():
    op.drop_table('stores')
