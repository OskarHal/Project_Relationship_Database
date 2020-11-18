import sqlalchemy as sa
from sqlalchemy.orm import relationship
from db import Base


class CompanyCustomer(Base):
    __tablename__ = 'company_customers'
    customer_id = sa.Column(sa.Integer, sa.ForeignKey('customers.customer_id'), autoincrement=False, primary_key=True,ondelete= 'CASCADE', onupdate='CASCADE')
    company_customer_name = sa.Column(sa.String(100), nullable=False)
    company_customer_first_name = sa.Column(sa.String(45), nullable=False)
    company_customer_last_name = sa.Column(sa.String(45), nullable=False)
    company_customer_email = sa.Column(sa.String(100), nullable=False)
    company_customer_phone = sa.Column(sa.String(45), nullable=False)
    customer = relationship("Customer", back_populates="comp_customer")

    def __repr__(self):
        return f'Customer ID={self.customer_id}, ' \
               f'Company Name={self.company_customer_name}, ' \
               f'Company Contact Name={self.company_customer_first_name} {self.company_customer_last_name}', \
               f'Company Contact Email={self.company_customer_email})', \
               f'Company Contact PhoneNr={self.company_customer_phone})'
