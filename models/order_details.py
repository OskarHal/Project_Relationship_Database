import sqlalchemy as sa
from app.db import Base
from sqlalchemy.orm import relationship


class OrderDetail(Base):
    __tablename__ = 'order_details'
    order_id = sa.Column(sa.Integer, sa.ForeignKey('orders.order_id'), primary_key=True)
    spare_part_id = sa.Column(sa.Integer, sa.ForeignKey('spare_parts.spare_part_id'), primary_key=True)
    quantity = sa.Column(sa.Integer, nullable=False)
    spare_part = relationship('SparePart')



class order(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    spare_parts = relationship("OrderDetails")

class sparepart(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)