"""create association order_details

Revision ID: 47a60b5d7746
Revises: 13f349b7b134
Create Date: 2020-11-17 15:07:19.351995

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '47a60b5d7746'
down_revision = '13f349b7b134'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'order_details',
        sa.Column('order_id', sa.Integer, sa.ForeignKey('orders.order_id'), primary_key=True),
        sa.Column('spare_part_id', sa.Integer, sa.ForeignKey('spare_parts.spare_part_id'), primary_key=True),
        sa.Column('quantity', sa.Integer, nullable=False)
    )


def downgrade():
    op.drop_table('order_details')
