import sqlalchemy as sa
from sqlalchemy.orm import relationship
from db import Base


class Order(Base):
    __tablename__ = 'orders'
    order_id = sa.Column(sa.Integer, primary_key=True)
    customer_id = sa.Column(sa.Integer, sa.ForeignKey('customers.customer_id'), nullable=True)
    employee_id = sa.Column(sa.Integer, sa.ForeignKey('employees.employee_id'), nullable=True)
    store_id = sa.Column(sa.Integer, sa.ForeignKey('stores.store_id'), nullable=True)
    order_date = sa.Column(sa.DateTime, default="CURRENT_TIMESTAMP", nullable=False)
    customer = relationship("Customer", back_populates="orders")
    employees = relationship("Employee", back_populates="orders")
    stores = relationship("Store", back_populates="orders")
    spare_parts = relationship("OrderDetails")


def __repr__(self):
    return f'Order(OrderId={self.order_id}, ' \
           f'customer_id={self.customer_id}, ' \
           f'employee_id={self.employee_id} ', \
           f'store_id={self.store_id} ', \
           f'order_date={self.order_date}) ',
