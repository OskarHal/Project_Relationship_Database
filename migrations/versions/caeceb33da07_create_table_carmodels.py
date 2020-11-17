"""create table carmodels

Revision ID: caeceb33da07
Revises: 
Create Date: 2020-11-17 11:55:11.047562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'caeceb33da07'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'carmodels',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('employee_id', sa.Integer, sa.ForeignKey('employees.id')),
        sa.Column('store_id', sa.Integer, sa.ForeignKey('stores.id'))
    )


def downgrade():
    pass
