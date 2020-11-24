"""Create car_models_sparepart table

Revision ID: ef5cb49d9a08
Revises: 14970569c9de
Create Date: 2020-11-24 13:52:04.624482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef5cb49d9a08'
down_revision = '14970569c9de'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'car_models_spare_parts',
        sa.Column('car_model_id', sa.Integer, sa.ForeignKey('car_models.car_model_id', ondelete='RESTRICT', onupdate='CASCADE')),
        sa.Column('spare_part_id', sa.Integer, sa.ForeignKey('spare_parts.spare_part_id', ondelete='RESTRICT', onupdate='NO ACTION')),
    )


def downgrade():
    op.drop_table('car_models_spare_parts')
