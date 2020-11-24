"""Create stores table

Revision ID: 9df13975cf63
Revises: ceb74a11d5c4
Create Date: 2020-11-24 13:19:46.892538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9df13975cf63'
down_revision = 'ceb74a11d5c4'
branch_labels = None
depends_on = None




def upgrade():
    op.create_table(
        'stores',
        sa.Column('store_id', sa.Integer, primary_key=True),
        sa.Column('store_name', sa.String(45), nullable=False),
        sa.Column('store_phone_nr', sa.String(45), nullable=False),
        sa.Column('store_email', sa.String(45), nullable=False),
        sa.Column('store_address', sa.String(45), nullable=False)
    )


def downgrade():
    op.drop_table('stores')