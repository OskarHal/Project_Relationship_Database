import sqlalchemy as sa
from sqlalchemy.orm import relationship
from db import Base


class SparePartStore(Base):
    __tablename__ = 'spare_part_stores'
    store_id = sa.Column(sa.Integer, sa.ForeignKey('stores.store_id'), primary_key=True)
    spare_part_id = sa.Column(sa.Integer, sa.ForeignKey('spare_parts.spare_part_id'), primary_key=True)
    stock = sa.Column(sa.Integer, nullable=False)
    stock_location = sa.Column(sa.String(45), nullable=False)
    spare_part = relationship('SparePart', back_populates="stores")
    store = relationship('Store', back_populates="spare_parts")

