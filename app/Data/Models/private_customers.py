import sqlalchemy as sa
from sqlalchemy.orm import relationship
from db import Base


class PrivateCustomer(Base):
    __tablename__ = 'private_customers'
    customer_id = sa.Column(sa.Integer, sa.ForeignKey("customers.customer_id"), primary_key=True, autoincrement=False,ondelete= 'CASCADE', onupdate='CASCADE')
    private_customer_first_name = sa.Column(sa.String(45), nullable=False)
    private_customer_last_name = sa.Column(sa.String(45), nullable=False)
    private_customer_phone = sa.Column(sa.String(45), nullable=False)
    private_customer_email = sa.Column(sa.String(100), nullable=False)
    customer = relationship("Customer", back_populates="customer")

    def __repr__(self):
        return f'Customer ID={self.customer_id}, ' \
               f'Private customer first name={self.private_customer_first_name}, ' \
               f'Private customer last name={self.private_customer_last_name}, ' \
               f'Private customer phone={self.private_customer_phone}, ' \
               f'Private customer email={self.private_customer_email}, '
