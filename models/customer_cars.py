import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app import Base


class CustomerCar(Base):
    __tablename__ = 'customer_cars'
    registration_nr = sa.Column(sa.String(45), primary_key=True, autoincrement=False)
    customer_car_brand = sa.Column(sa.String(45), nullable=False)
    customer_car_model = sa.Column(sa.String(45), nullable=False)
    customer_car_model_year = sa.Column(sa.Integer, nullable=False)
    customer_car_color = sa.Column(sa.String(45), nullable=False)
    customer_id = sa.Column(sa.Integer, sa.ForeignKey("customers.customer_id"))
    owner = relationship("Customer", back_populates="cars")

    def __repr__(self):
        return f'Registration number={self.registration_nr}, ' \
               f'Car brand={self.customer_car_brand}, ' \
               f'Car Model={self.customer_car_model} ', \
               f'Model year={self.customer_car_model_year}', \
               f'Color={self.customer_car_color}',

