"""create association spare_part_stores

Revision ID: ff7ee8b9312d
Revises: 47a60b5d7746
Create Date: 2020-11-17 15:07:22.025487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff7ee8b9312d'
down_revision = '47a60b5d7746'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'spare_part_stores',
        sa.Column('store_id', sa.Integer, sa.ForeignKey('stores.store_id'), primary_key=True),
        sa.Column('spare_part_id', sa.Integer, sa.ForeignKey('spare_parts.spare_part_id'), primary_key=True),
        sa.Column('stock', sa.Integer, nullable=False),
        sa.Column('stock_location', sa.String(45), nullable=False)
    )


def downgrade():
    op.drop_table('spare_part_stores')
