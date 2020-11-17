import sqlalchemy as sa
from sqlalchemy.orm import relationship
from db import Base


class Employee(Base):
    __tablename__ = 'employees'
    employee_id = sa.Column(sa.Integer, primary_key=True)
    employee_name = sa.Column(sa.String(45), nullable=False)
    employee_lastname = sa.Column(sa.String(45), nullable=False)
    employee_phone_nr = sa.Column(sa.String(45), nullable=False)
    employee_email = sa.Column(sa.String(45), nullable=False)
    store = relationship("Store", back_populates="employees")
    orders = relationship("Order", back_populates="employees")

    def __repr__(self):
        return f'Employee(employee_id ={self.employee_id}, ' \
               f'employee_name={self.employee_name}, ' \
               f'employee_lastname={self.employee_lastname} ', \
               f'employee_phone_nr={self.employee_phone_nr})',\
               f'employee_email={self.employee_email})',
