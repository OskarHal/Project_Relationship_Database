"""create table employees

Revision ID: 13f349b7b134
Revises: 96f9536c7d9c
Create Date: 2020-11-17 15:07:16.674454

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '13f349b7b134'
down_revision = '96f9536c7d9c'
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
        sa.Column('store_id', sa.Integer, sa.ForeignKey("stores.store_id"))
    )


def downgrade():
    op.drop_table('employees')
