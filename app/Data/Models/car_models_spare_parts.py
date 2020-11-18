import sqlalchemy as sa
from db import Base

car_models_spare_parts = sa.Table(
    'car_models_spare_parts',
    Base.metadata,
    sa.Column('car_model_id', sa.Integer, sa.ForeignKey('car_models.car_model_id')),
    sa.Column('spare_part_id', sa.Integer, sa.ForeignKey('spare_parts.spare_part_id'))
)
