"""'car_models'

Revision ID: 00c965f8a807
Revises: 
Create Date: 2020-11-17 11:46:16.774988

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '00c965f8a807'
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
