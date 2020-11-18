import sqlalchemy as sa
from sqlalchemy.orm import relationship
from db import Base


class Customer(Base):
    __tablename__ = 'customers'
    customer_id = sa.Column(sa.Integer, primary_key=True)
    customer_type = sa.Column(sa.Integer, nullable=False)
    cars = relationship("CustomerCar", back_populates="owner")
    orders = relationship("Order", back_populates="customer")
    comp_customer = relationship("CompanyCustomer", back_populates="customer")
    priv_customer = relationship("PrivateCustomer", back_populates="customer")

    # TESTA MED @property

    def __repr__(self):
        if self.customer_type == 1:
            return f'Customer ID={self.customer_id}, Company Customer'
                    # f'Owns cars with registration number: {self.cars.registration_nr}'
        else:
            return f'Customer ID={self.customer_id}, Private Customer'
                    # f'Owns cars with registration number: {self.cars.registration_nr}'


