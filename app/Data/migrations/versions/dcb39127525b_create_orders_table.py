"""Create orders table

Revision ID: dcb39127525b
Revises: 2d62deb45bbc
Create Date: 2020-11-24 13:20:28.993652

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = 'dcb39127525b'
down_revision = '2d62deb45bbc'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'orders',
        sa.Column('order_id', sa.Integer, primary_key=True),
        sa.Column('customer_id', sa.Integer, sa.ForeignKey('customers.customer_id', ondelete='SET NULL', onupdate='CASCADE'), nullable=True),
        sa.Column('employee_id', sa.Integer, sa.ForeignKey('employees.employee_id', ondelete='SET NULL', onupdate='CASCADE'), nullable=True),
        sa.Column('store_id', sa.Integer, sa.ForeignKey('stores.store_id', ondelete='SET NULL', onupdate='CASCADE'), nullable=True),
        sa.Column('order_date', sa.DateTime, default=datetime.utcnow, nullable=False)
    )


def downgrade():
    op.drop_table('orders')
