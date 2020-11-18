import sqlalchemy as sa
from sqlalchemy.orm import relationship
from Data.db import Base


class ManufacturerContact(Base):
    __tablename__ = 'company_contacts'
    manufacturer_contact_id = sa.Column(sa.Integer, primary_key=True)
    manufacturer_contact_name = sa.Column(sa.String(100), nullable=False)
    manufacturer_contact_phone_nr = sa.Column(sa.String(45), nullable=True)
    manufacturer_contact_email = sa.Column(sa.String(100), nullable=True)
    manufacturer_id = sa.Column(sa.Integer, sa.ForeignKey("manufacturers.manufacturer_id"), onupdate='CASCADE', ondelete='CASCADE')
    manufacturer = relationship("Manufacturer", back_populates="company_contacts")

    def __repr__(self):
        return f'manufacturer_contact(company_contact_id={self.manufacturer_contact_id}, ' \
               f'manufacturer_contact_name={self.manufacturer_contact_name}, ' \
               f'manufacturer_phone_nr={self.manufacturer_contact_phone_nr})' \
               f'manufacturer_email={self.manufacturer_contact_email})' \
