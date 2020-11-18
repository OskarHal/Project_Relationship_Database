"""create table company_customers

Revision ID: d4923409e782
Revises: 92e62e07f010
Create Date: 2020-11-17 15:07:05.604813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4923409e782'
down_revision = '92e62e07f010'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'company_customers',
        sa.Column('customer_id', sa.Integer, sa.ForeignKey('customers.customer_id'), autoincrement=False, primary_key=True),
        sa.Column('company_customer_name', sa.String(100), nullable=False),
        sa.Column('company_customer_first_name', sa.String(45), nullable=False),
        sa.Column('company_customer_last_name', sa.String(45), nullable=False),
        sa.Column('company_customer_email', sa.String(100), nullable=False),
        sa.Column('company_customer_phone', sa.String(45), nullable=False),
    )


def downgrade():
    op.drop_table('company_customers)
