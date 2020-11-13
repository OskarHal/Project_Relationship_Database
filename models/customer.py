import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.db import Base


class Customer(Base):
    __tablename__ = 'customers'
    customer_id = sa.Column(sa.Integer, primary_key=True)
    customer_type = sa.Column(sa.Integer, nullable=False)
    customer = relationship(
        "CompanyCustomer", "PrivateCustomer", back_populates=["company_customer", "private_customer"])

    def __repr__(self):
        if self.customer_type == 1:
            return f'Customer ID={self.customer_id}, Company Customer'
        else:
            return f'Customer ID={self.customer_id}, Private Customer'
