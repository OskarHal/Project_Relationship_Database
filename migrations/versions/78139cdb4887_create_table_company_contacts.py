"""create table company_contacts

Revision ID: 78139cdb4887
Revises: f7d7ce05712f
Create Date: 2020-11-17 15:06:45.144470

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '78139cdb4887'
down_revision = 'f7d7ce05712f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'company_contacts',
        sa.Column('manufacturer_contact_id', sa.Integer, primary_key=True),
        sa.Column('manufacturer_contact_name', sa.String(100), nullable=False),
        sa.Column('manufacturer_contact_phone_nr', sa.String(45), nullable=True),
        sa.Column('manufacturer_contact_email', sa.String(100), nullable=True),
        sa.Column(sa.Integer, sa.ForeignKey('manufacturer_id', "manufacturers.manufacturer_id"))
    )


def downgrade():
    op.drop_table('company_contacts')
