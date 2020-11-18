import sqlalchemy as sa
from sqlalchemy.orm import relationship
from db import Base


class Manufacturer(Base):
    __tablename__ = 'manufacturers'
    manufacturer_id = sa.Column(sa.Integer, primary_key=True)
    manufacturer_name = sa.Column(sa.String(45), nullable=False)
    manufacturer_phone_nr = sa.Column(sa.String(45), nullable=True)
    manufacturer_address = sa.Column(sa.String(100), nullable=False)
    company_contacts = relationship("ManufacturerContact", back_populates="manufacturer")
    spare_parts = relationship("SparePart", back_populates="manufacturer")

    def __repr__(self):
        return f'Manufacturer(manufacturer_id={self.manufacturer_id}, ' \
               f'manufacturer_name={self.manufacturer_name}, ' \
               f'phone_nr={self.manufacturer_phone_nr} ', \
               f'address={self.manufacturer_address})',
