import sqlalchemy as sa
from sqlalchemy.orm import relationship
from Data.db import Base
from .car_models_spare_parts import car_models_spare_parts


class SparePart(Base):
    __tablename__ = 'spare_parts'
    spare_part_id = sa.Column(sa.Integer, primary_key=True)
    product_nr = sa.Column(sa.String(45), nullable=False)
    description = sa.Column(sa.String(255), nullable=True)
    purchase_price = sa.Column(sa.FLOAT, nullable=False)
    selling_price = sa.Column(sa.FLOAT, nullable=False)
    reorder_level = sa.Column(sa.Integer, nullable=True)
    order_quantity = sa.Column(sa.Integer, nullable=True)
    estimated_time_of_arrival = sa.Column(sa.DATE, nullable=True)
    manufacturer_id = sa.Column(sa.Integer, sa.ForeignKey('manufacturers.manufacturer_id', ondelete='SET NULL', onupdate='CASCADE'))
    supplier_id = sa.Column(sa.Integer, sa.ForeignKey('suppliers.supplier_id', ondelete='SET NULL', onupdate='CASCADE'))
    manufacturer = relationship("Manufacturer", back_populates="spare_parts")
    supplier = relationship("Supplier", back_populates="spare_parts")
    stores = relationship("SparePartStore", back_populates="spare_part", cascade="all, delete")
    car_models = relationship("CarModel", secondary=car_models_spare_parts, back_populates="spare_parts")
    order_detail = relationship("OrderDetail", back_populates="spare_part", cascade="all, delete")

    def __repr__(self):
        return f'SparePart(spare_part_id={self.spare_part_id},' \
               f'product_nr={self.product_nr}, ' \
               f'manufacturer_id={self.manufacturer_id}, ' \
               f'supplier_id={self.supplier_id}, ' \
               f'purchase_price={self.purchase_price} ' \
               f'selling_price={self.selling_price} ' \
               f'reorder_level={self.reorder_level} ' \
               f'order_quantity={self.order_quantity})'

    def print_all_information_with_relationships(self):
        print(f"Product number {self.product_nr}".center(45, '#'))
        print((30 + len("Information")) * "-")
        print('Category'.ljust(30), end="|")
        print("Information")
        print((30 + len("Information")) * "-")
        print(f"Id: ".ljust(30), end='|')
        print(f"{self.spare_part_id}")
        print(f"Description: ".ljust(30), end='|')
        print(f"{self.description}")
        print(f"Purchase price ".ljust(30), end='|')
        print(f"{self.purchase_price}")
        print(f"Selling price".ljust(30), end='|')
        print(f"{self.selling_price}")
        print(f"Reorder level".ljust(30), end='|')
        print(f"{self.reorder_level}")
        print(f"Order quantity".ljust(30), end='|')
        print(f"{self.order_quantity}")
        print(f"Estimated time of arrival".ljust(30), end='|')
        print(f"{self.estimated_time_of_arrival}")
        print(f"Manufacturer".ljust(30), end='|')
        print(f"{self.manufacturer.manufacturer_name}")
        print(f"Supplier".ljust(30), end='|')
        print(f"{self.supplier.supplier_name}")
        print((30 + len("Information")) * "-")
        print("Availability".center(60))
        print((60 + len("Availability")) * "-")
        print('Store'.ljust(30), end="")
        print("Store location".ljust(30), end="")
        print("Stock")
        print((60 + len("Availability")) * "-")

        for spare_part_store in self.stores:
            print(spare_part_store.store.store_name.ljust(30), end="")
            print(spare_part_store.stock_location.ljust(30), end="")
            print(f"{spare_part_store.stock} items")

