"""Create company_contacts table

Revision ID: b47ec1d85acb
Revises: 75e879230a07
Create Date: 2020-11-24 13:15:01.726894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b47ec1d85acb'
down_revision = '75e879230a07'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'company_contacts',
        sa.Column('manufacturer_contact_id', sa.Integer, primary_key=True),
        sa.Column('manufacturer_contact_name', sa.String(100), nullable=False),
        sa.Column('manufacturer_contact_phone_nr', sa.String(45), nullable=True),
        sa.Column('manufacturer_contact_email', sa.String(100), nullable=True),
        sa.Column('manufacturer_id', sa.Integer, sa.ForeignKey("manufacturers.manufacturer_id",onupdate='CASCADE', ondelete='CASCADE'))
    )


def downgrade():
    op.drop_table('company_contacts')
