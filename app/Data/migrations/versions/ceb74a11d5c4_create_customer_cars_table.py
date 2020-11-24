"""Create customer_cars table

Revision ID: ceb74a11d5c4
Revises: c48c0aebb460
Create Date: 2020-11-24 13:18:35.243361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ceb74a11d5c4'
down_revision = 'c48c0aebb460'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'customer_cars',
        sa.Column('registration_nr', sa.String(45), primary_key=True, autoincrement=False),
        sa.Column('customer_car_brand', sa.String(45), nullable=False),
        sa.Column('customer_car_model', sa.String(45), nullable=False),
        sa.Column('customer_car_model_year', sa.Integer, nullable=False),
        sa.Column('customer_car_color', sa.String(45), nullable=False),
        sa.Column('customer_id', sa.Integer, sa.ForeignKey("customers.customer_id", ondelete='CASCADE', onupdate='CASCADE'))
    )


def downgrade():
    op.drop_table('customer_cars')