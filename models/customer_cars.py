import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.db import Base


class CustomerCar(Base):
    __tablename__ = 'customer_cars'
    registration_nr = sa.Column(sa.String(45), primary_key=True, autoincrement=False)
    customer_id = sa.Column(sa.Integer, sa.ForeignKey("customers.customer_id"))
    brand = sa.Column(sa.String(45), nullable=False)
    model = sa.Column(sa.String(45), nullable=False)
    model_year = sa.Column(sa.Integer, nullable=False)
    color = sa.Column(sa.String(45), nullable=False)
    owner = relationship("Customer", back_populates="cars")

    def __repr__(self):
        return f'Registration number={self.registration_nr}, ' \
               f'Car brand={self.brand}, ' \
               f'Car Model={self.model} ', \
               f'Model year={self.model_year}', \
               f'Color={self.color}',

