"""create table customer_cars

Revision ID: 47c8c0cfd387
Revises: 97ac442cfd5a
Create Date: 2020-11-17 15:06:54.128954

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '47c8c0cfd387'
down_revision = '97ac442cfd5a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'customer_cars',
        sa.Column('registration_nr', sa.String(45), primary_key=True, autoincrement=False),
        sa.Column('customer_car_brand'.sa.String(45), nullable=False),
        sa.Column('customer_car_model', sa.String(45), nullable=False),
        sa.Column('customer_car_model_year', sa.Integer, nullable=False),
        sa.Column('customer_car_color', sa.String(45), nullable=False),
        sa.Column('customer_id', sa.Integer, sa.ForeignKey("customers.customer_id"))
    )


def downgrade():
    op.drop_table('customer_cars')
