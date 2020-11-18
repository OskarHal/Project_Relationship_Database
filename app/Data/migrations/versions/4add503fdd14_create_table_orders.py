"""create table orders

Revision ID: 4add503fdd14
Revises: d4923409e782
Create Date: 2020-11-17 15:07:09.710487

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '4add503fdd14'
down_revision = 'd4923409e782'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'orders',
        sa.Column('order_id', sa.Integer, primary_key=True),
        sa.Column('customer_id', sa.Integer, sa.ForeignKey('customers.customer_id'), nullable=True),
        sa.Column('employee_id', sa.Integer, sa.ForeignKey('employees.employee_id'), nullable=True),
        sa.Column('store_id', sa.Integer, sa.ForeignKey('stores.store_id'), nullable=True),
        sa.Column('order_date', sa.DateTime, default=datetime.utcnow, nullable=False)
    )


def downgrade():
    op.drop_table('orders')
