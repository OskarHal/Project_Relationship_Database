import sqlalchemy as sa
from Data.db import Base
from sqlalchemy.orm import relationship


class OrderDetail(Base):
    __tablename__ = 'order_details'
    order_id = sa.Column(sa.Integer, sa.ForeignKey('orders.order_id', ondelete='NO ACTION', onupdate='NO ACTION'),primary_key=True)
    spare_part_id = sa.Column(sa.Integer, sa.ForeignKey('spare_parts.spare_part_id', ondelete='NO ACTION', onupdate='NO ACTION'), primary_key=True,)
    quantity = sa.Column(sa.Integer, nullable=False)
    spare_part = relationship('SparePart', back_populates="order_detail")
    order = relationship('Order', back_populates="order_lines")
