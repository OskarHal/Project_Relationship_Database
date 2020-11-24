"""Create private_customers table

Revision ID: a4408b1c893e
Revises: a68480028d11
Create Date: 2020-11-24 13:17:39.545221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4408b1c893e'
down_revision = 'a68480028d11'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'private_customers',
        sa.Column('customer_id', sa.Integer, sa.ForeignKey("customers.customer_id", ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, autoincrement=False),
        sa.Column('private_customer_first_name', sa.String(45), nullable=False),
        sa.Column('private_customer_last_name', sa.String(45), nullable=False),
        sa.Column('private_customer_phone', sa.String(45), nullable=False),
        sa.Column('private_customer_email', sa.String(100), nullable=False)
    )


def downgrade():
    op.drop_table('private_customers')
