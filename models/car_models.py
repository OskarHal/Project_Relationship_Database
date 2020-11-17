import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.db import Base
from models import car_models_spare_parts


class CarModel(Base):
    __tablename__ = 'car_models'
    car_model_id = sa.Column(sa.Integer, primary_key=True)
    model_name = sa.Column(sa.String(45), nullable=True)
    brand_name = sa.Column(sa.String(45), nullable=True)
    spare_parts = relationship("SparePart", secondary=car_models_spare_parts, back_populates="car_models")

    def __repr__(self):
        return f'CarModel(car_model_id={self.car_model_id}, ' \
               f'model_name={self.model_name}, ' \
               f'brand_name={self.brand_name})'
