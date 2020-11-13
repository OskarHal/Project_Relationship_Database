import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.db import Base


class Manufacturer(Base):
    __tablename__ = 'manufacturers'
    manufacturer_id = sa.Column(sa.Integer, primary_key=True)
    manufacturer_name = sa.Column(sa.String(100), nullable=False)
    phone_nr = sa.Column(sa.String(45), nullable=False)
    address = sa.Column(sa.String(45), nullable=False)
    spare_parts = relationship("SparePart", back_populates="manufacturer")

    def __repr__(self):
        return f'Manufacturer(manufacturer_id={self.manufacturer_id}, ' \
               f'manufacturer_name={self.manufacturer_name}, ' \
               f'phone_nr={self.phone_nr} ', \
               f'address={self.address})',
