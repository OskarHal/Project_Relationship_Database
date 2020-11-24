"""Create spare_part_stores table

Revision ID: 14970569c9de
Revises: 0d9cc4ba9229
Create Date: 2020-11-24 13:21:49.279647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14970569c9de'
down_revision = '0d9cc4ba9229'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'spare_part_stores',
        sa.Column('store_id', sa.Integer, sa.ForeignKey('stores.store_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True),
        sa.Column('spare_part_id', sa.Integer, sa.ForeignKey('spare_parts.spare_part_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True),
        sa.Column('stock', sa.Integer, nullable=False),
        sa.Column('stock_location', sa.String(45), nullable=False)
    )


def downgrade():
    op.drop_table('spare_part_stores')