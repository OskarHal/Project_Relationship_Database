"""create table manufacturers

Revision ID: f7d7ce05712f
Revises: b45264bc0b96
Create Date: 2020-11-17 15:06:41.441973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7d7ce05712f'
down_revision = 'b45264bc0b96'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'manufacturers',
        sa.Column('manufacturer_id', sa.Integer, primary_key=True),
        sa.Column('manufacturer_name', sa.String(45), nullable=False),
        sa.Column('manufacturer_phone_nr', sa.String(45), nullable=True),
        sa.Column('manufacturer_address', sa.String(100), nullable=False)
    )


def downgrade():
    op.drop_table('manufacturers')
