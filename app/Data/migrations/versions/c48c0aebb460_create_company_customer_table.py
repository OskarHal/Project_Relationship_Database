"""Create company_customer table

Revision ID: c48c0aebb460
Revises: a4408b1c893e
Create Date: 2020-11-24 13:18:02.178734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c48c0aebb460'
down_revision = 'a4408b1c893e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'company_customers',
        sa.Column('customer_id', sa.Integer, sa.ForeignKey('customers.customer_id', ondelete='CASCADE', onupdate='CASCADE'), autoincrement=False, primary_key=True),
        sa.Column('company_customer_name', sa.String(100), nullable=False),
        sa.Column('company_customer_first_name', sa.String(45), nullable=False),
        sa.Column('company_customer_last_name', sa.String(45), nullable=False),
        sa.Column('company_customer_email', sa.String(100), nullable=False),
        sa.Column('company_customer_phone', sa.String(45), nullable=False),
    )


def downgrade():
    op.drop_table('company_customers')
