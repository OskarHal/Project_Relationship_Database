"""create table carmodels

Revision ID: d248229298a2
Revises: 
Create Date: 2020-11-17 15:06:22.841987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd248229298a2'
down_revision = None
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