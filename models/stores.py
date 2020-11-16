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
    employees = relationship("Employee", back_populates="store")
    spare_parts = relationship("SparePartStore", back_populates="store")


    def __repr__(self):
        return f'Store(store_id={self.store_id}, ' \
               f'store_name={self.store_name}, ' \
               f'store_phone_nr={self.store_phone_nr} ', \
               f'store_email={self.store_email} ', \
               f'store_address={self.store_address}) ',


    class Association(Base):
        tablename = 'spare_part_stores'
        left_id = Column(Integer, ForeignKey('left.id'), primary_key=True)
        right_id = Column(Integer, ForeignKey('right.id'), primary_key=True)
        extra_data = Column(String(50))
        child = relationship("Child", back_populates="parents")
        parent = relationship("Parent", back_populates="children")

    class Parent(Base):
        tablename = 'left'
        id = Column(Integer, primary_key=True)
        children = relationship("Association", back_populates="parent")

    class Child(Base):
        tablename = 'right'
        id = Column(Integer, primary_key=True)
        parents = relationship("Association", back_populates="child")


    class Association(Base):
        tablename = 'association'
        left_id = Column(Integer, ForeignKey('left.id'), primary_key=True)
        right_id = Column(Integer, ForeignKey('right.id'), primary_key=True)
        extra_data = Column(String(50))
        child = relationship("Child", back_populates="parents")
        parent = relationship("Parent", back_populates="children")

    class Parent(Base):
        tablename = 'left'
        id = Column(Integer, primary_key=True)
        children = relationship("Association", back_populates="parent")

    class Child(Base):
        tablename = 'right'
        id = Column(Integer, primary_key=True)
        parents = relationship("Association", back_populates="child")
