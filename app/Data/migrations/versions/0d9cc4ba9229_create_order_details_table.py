"""Create order_details table

Revision ID: 0d9cc4ba9229
Revises: dcb39127525b
Create Date: 2020-11-24 13:21:02.344151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d9cc4ba9229'
down_revision = 'dcb39127525b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'order_details',
        sa.Column('order_id', sa.Integer, sa.ForeignKey('orders.order_id', ondelete='NO ACTION', onupdate='NO ACTION'), primary_key=True),
        sa.Column('spare_part_id', sa.Integer, sa.ForeignKey('spare_parts.spare_part_id', ondelete='NO ACTION', onupdate='NO ACTION'), primary_key=True),
        sa.Column('quantity', sa.Integer, nullable=False)
    )


def downgrade():
    op.drop_table('order_details')