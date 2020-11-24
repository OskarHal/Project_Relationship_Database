"""Create car_models table

Revision ID: 914432d81965
Revises: 9bb1f24f8f37
Create Date: 2020-11-24 13:16:34.742694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '914432d81965'
down_revision = '9bb1f24f8f37'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'car_models',
        sa.Column('car_model_id', sa.Integer, primary_key=True),
        sa.Column('model_name', sa.String(45), nullable=True),
        sa.Column('brand_name', sa.String(45), nullable=True)
    )


def downgrade():
    op.drop_table('car_models')
