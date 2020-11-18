import sqlalchemy as sa
from db import Base
from sqlalchemy.orm import relationship


class OrderDetail(Base):
    __tablename__ = 'order_details'
    order_id = sa.Column(sa.Integer, sa.ForeignKey('orders.order_id'), primary_key=True,ondelete= 'NO ACTION', onupdate='NO ACTION')
    spare_part_id = sa.Column(sa.Integer, sa.ForeignKey('spare_parts.spare_part_id'), primary_key=True,ondelete='NO ACTION', onupdate='NO ACTION')
    quantity = sa.Column(sa.Integer, nullable=False)
    spare_part = relationship('SparePart')
