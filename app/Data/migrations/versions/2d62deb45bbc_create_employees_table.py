"""Create employees table

Revision ID: 2d62deb45bbc
Revises: 9df13975cf63
Create Date: 2020-11-24 13:20:09.257961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d62deb45bbc'
down_revision = '9df13975cf63'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'employees',
        sa.Column('employee_id', sa.Integer, primary_key=True),
        sa.Column('employee_name', sa.String(45), nullable=False),
        sa.Column('employee_lastname', sa.String(45), nullable=False),
        sa.Column('employee_phone_nr', sa.String(45), nullable=False),
        sa.Column('employee_email', sa.String(45), nullable=False),
        sa.Column('store_id', sa.Integer, sa.ForeignKey("stores.store_id", ondelete='SET NULL', onupdate='CASCADE'))
    )


def downgrade():
    op.drop_table('employees')
