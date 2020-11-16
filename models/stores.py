import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.db import Base

'''   

class Parent(Base):
 children = relationship("Child", back_populates="parent")

'''
class Store(Base):
    __tablename__ = 'stores'
    store_id = sa.Column(sa.Integer, primary_key=True)
    store_name = sa.Column(sa.String(45), nullable=False)
    store_phone_nr = sa.Column(sa.String(45), nullable=False)
    store_email = sa.Column(sa.String(45), nullable=False)
    store_address = sa.Column(sa.String(45), nullable=False)

    employees = relationship(
        "Employee",
     back_populates='store')

    spare_parts = relationship(
        "SparePart",

        back_populates="car_models")



    def __repr__(self):
        return f'Store(store_id={self.store_id}, ' \
               f'store_name={self.store_name}, ' \
               f'store_phone_nr={self.store_phone_nr} ', \
               f'store_email={self.store_email} ', \
               f'store_address={self.store_address}) ',
