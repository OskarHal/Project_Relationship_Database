import sqlalchemy as sa
from sqlalchemy.orm import relationship
from Data.db import Base


class Supplier(Base):
    __tablename__ = 'suppliers'
    supplier_id = sa.Column(sa.Integer, primary_key=True)
    supplier_name = sa.Column(sa.String(45), nullable=False)
    supplier_phone_nr = sa.Column(sa.String(45), nullable=True)
    supplier_email = sa.Column(sa.String(100), nullable=True)
    supplier_address = sa.Column(sa.String(100), nullable=False)
    supplier_contact_first_name = sa.Column(sa.String(100), nullable=True)
    supplier_contact_last_name = sa.Column(sa.String(100), nullable=True)
    spare_parts = relationship("SparePart", back_populates="supplier")

    def __repr__(self):
        return f'Supplier(SupplierId={self.supplier_id}, ' \
               f'supplier_name={self.supplier_name}, ' \
               f'supplier phone_nr={self.supplier_phone_nr}, ' \
               f'supplier email={self.supplier_email}, ' \
               f'supplier address={self.supplier_address}), ' \
               f'supplier contact_first_name={self.supplier_contact_first_name}), ' \
               f'supplier contact_last_name={self.supplier_contact_last_name}),'
