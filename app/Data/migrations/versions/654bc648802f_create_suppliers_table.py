"""Create suppliers table

Revision ID: 654bc648802f
Revises: b47ec1d85acb
Create Date: 2020-11-24 13:15:38.372163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '654bc648802f'
down_revision = 'b47ec1d85acb'
branch_labels = None
depends_on = None



def upgrade():
    op.create_table(
        'suppliers',
        sa.Column('supplier_id', sa.Integer, primary_key=True),
        sa.Column('supplier_name', sa.String(45), nullable=False),
        sa.Column('supplier_phone_nr', sa.String(45), nullable=True),
        sa.Column('supplier_email', sa.String(100), nullable=True),
        sa.Column('supplier_address', sa.String(100), nullable=False),
        sa.Column('supplier_contact_first_name', sa.String(100), nullable=True),
        sa.Column('supplier_contact_last_name', sa.String(100), nullable=True)
    )


def downgrade():
    op.drop_table('suppliers')


