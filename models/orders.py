import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.db import Base

'''class Child(Base):
    tablename = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Parent", back_populates="children")'''


class Order(Base):
    __tablename__ = 'orders'
    order_id = sa.Column(sa.Integer, primary_key=True)
    customer_id = sa.Column(sa.Integer, sa.ForeignKey('customers.customer_id'), nullable=True)
    employee_id = sa.Column(sa.Integer, sa.ForeignKey('employees.employee_id'), nullable=True)
    store_id = sa.Column(sa.Integer, sa.ForeignKey('stores.store_id'), nullable=True)
    order_date = sa.Column(sa.DateTime, nullable=False)

    customers = relationship(
        "Customer",
        back_populates="orders")

    employees = relationship(
        "Employee",
        back_populates="orders")

    stores = relationship(
        "Store",
        back_populates="orders")

    spare_parts = relationship(
        "OrderDetails")


def __repr__(self):
    return f'Order(OrderId={self.order_id}, ' \
           f'customer_id={self.customer_id}, ' \
           f'employee_id={self.employee_id} ', \
           f'store_id={self.store_id} ', \
           f'order_date={self.order_date}) ',
