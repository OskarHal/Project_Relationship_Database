"""create table suppliers

Revision ID: 97ac442cfd5a
Revises: 78139cdb4887
Create Date: 2020-11-17 15:06:49.448993

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '97ac442cfd5a'
down_revision = '78139cdb4887'
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
