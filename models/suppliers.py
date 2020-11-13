import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.db import Base


class Supplier(Base):
    __tablename__ = 'suppliers'
    supplier_id = sa.Column(sa.Integer, primary_key=True)
    supplier_name = sa.Column(sa.String(100), nullable=False)
    phone_nr = sa.Column(sa.String(45), nullable=True)
    email = sa.Column(sa.String(100), nullable=True)
    address = sa.Column(sa.String(100), nullable=True)
    contact_first_name = sa.Column(sa.String(100), nullable=True)
    contact_last_name = sa.Column(sa.String(100), nullable=True)
    spare_parts = relationship("SparePart", back_populates="supplier")

    def __repr__(self):
        return f'Supplier(SupplierId={self.supplier_id}, ' \
               f'supplier_name={self.supplier_name}, ' \
               f'phone_nr={self.phone_nr} ', \
               f'email={self.email} ', \
               f'address={self.address}) ', \
               f'contact_first_name={self.contact_first_name}) ', \
               f'contact_last_name={self.contact_last_name})',
