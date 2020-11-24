"""Create spare_parts table

Revision ID: 9bb1f24f8f37
Revises: 654bc648802f
Create Date: 2020-11-24 13:16:17.174626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bb1f24f8f37'
down_revision = '654bc648802f'
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
        sa.Column('manufacturer_id', sa.Integer, sa.ForeignKey('manufacturers.manufacturer_id', ondelete= 'SET NULL', onupdate='CASCADE')),
        sa.Column('supplier_id', sa.Integer, sa.ForeignKey('suppliers.supplier_id', ondelete= 'SET NULL', onupdate='CASCADE')),
    )


def downgrade():
    op.drop_table('spare_parts')

