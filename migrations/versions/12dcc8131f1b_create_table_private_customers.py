"""create table private_customers

Revision ID: 12dcc8131f1b
Revises: 47c8c0cfd387
Create Date: 2020-11-17 15:06:58.292974

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '12dcc8131f1b'
down_revision = '47c8c0cfd387'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'private_customers',
        sa.Column('customer_id', sa.Integer, sa.ForeignKey("customers.customer_id"), primary_key=True, autoincrement=False),
        sa.Column('private_customer_first_name', sa.String(45), nullable=False),
        sa.Column('private_customer_last_name', sa.String(45), nullable=False),
        sa.Column('private_customer_phone', sa.String(45), nullable=False),
        sa.Column('private_customer_email', sa.String(100), nullable=False)
    )


def downgrade():
    op.drop_table('private_customers')
