import sqlalchemy as sa
from sqlalchemy.orm import relationship
from Data.db import Base
from datetime import datetime
from .order_details import OrderDetail


class Order(Base):
    __tablename__ = 'orders'
    order_id = sa.Column(sa.Integer, primary_key=True)
    customer_id = sa.Column(sa.Integer, sa.ForeignKey('customers.customer_id'), nullable=True,ondelete= 'SET NULL', onupdate='CASCADE')
    employee_id = sa.Column(sa.Integer, sa.ForeignKey('employees.employee_id'), nullable=True,ondelete= 'SET NULL', onupdate='CASCADE')
    store_id = sa.Column(sa.Integer, sa.ForeignKey('stores.store_id'), nullable=True, ondelete= 'SET NULL', onupdate='CASCADE')
    order_date = sa.Column(sa.DateTime, default=datetime.utcnow, nullable=False)
    customer = relationship("Customer", back_populates="orders")
    employees = relationship("Employee", back_populates="orders")
    store = relationship("Store", back_populates="orders")
    spare_parts = relationship(OrderDetail)


def __repr__(self):
    return f'Order(OrderId={self.order_id}, ' \
           f'customer_id={self.customer_id}, ' \
           f'employee_id={self.employee_id} ', \
           f'store_id={self.store_id} ', \
           f'order_date={self.order_date}) ',
