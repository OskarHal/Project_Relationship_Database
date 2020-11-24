"""Create customer table

Revision ID: a68480028d11
Revises: 914432d81965
Create Date: 2020-11-24 13:17:05.490201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a68480028d11'
down_revision = '914432d81965'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'customers',
        sa.Column('customer_id', sa.Integer, primary_key=True),
        sa.Column('customer_type', sa.Integer, nullable=False)
    )


def downgrade():
    op.drop_table('customers')
