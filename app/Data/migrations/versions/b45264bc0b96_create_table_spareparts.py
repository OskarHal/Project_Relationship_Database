"""create table spareparts

Revision ID: b45264bc0b96
Revises: d248229298a2
Create Date: 2020-11-17 15:06:37.176470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b45264bc0b96'
down_revision = 'd248229298a2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'spare_parts',
        sa.Column('spare_part_id', sa.Integer, primary_key=True),
        sa.Column('product_nr', sa.String(45), nullable=False),
        sa.Column('description', sa.String(255), nullable=True),
        sa.Column('purchase_price', sa.FLOAT, nullable=False),
        sa.Column('selling_price', sa.FLOAT, nullable=False),
        sa.Column('reorder_level', sa.Integer, nullable=True),
        sa.Column('order_quantity', sa.Integer, nullable=True),
        sa.Column('estimated_time_of_arrival', sa.DATE, nullable=True),
        sa.Column('manufacturer_id', sa.Integer, sa.ForeignKey('manufacturers.manufacturer_id')),
        sa.Column('supplier_id', sa.Integer, sa.ForeignKey('suppliers.supplier_id')),
    )


def downgrade():
    op.drop_table('spare_parts')
