import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.db import Base
from models import car_models_spare_parts

'''class Child(Base):

 
    parent = relationship("Parent", back_populates="children")'''
class CompanyContact(Base):
    __tablename__ = 'company_contacts'
    company_contact_id = sa.Column(sa.Integer, primary_key=True)
    company_contact_name = sa.Column(sa.String(100), nullable=False)
    company_phone_nr = sa.Column(sa.String(45), nullable=True)
    company_email = sa.Column(sa.String(100), nullable=True)

    manufacturer = relationship("Manufacturer", back_populates="company_contacts")

    def __repr__(self):
        return f'company_contact(company_contact_id={self.company_contact_id}, ' \
               f'company_contact_name={self.company_contact_name}, ' \
               f'company_phone_nr={self.company_phone_nr})' \
               f' company_email={self.company_email})' \
