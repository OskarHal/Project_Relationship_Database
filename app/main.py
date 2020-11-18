from db import Base, engine, session
from models.manufacturers import Manufacturer
from models.company_contacts import ManufacturerContact
from models.suppliers import Supplier
from models.spare_parts import SparePart
from models.car_models import CarModel
from models.customer import Customer
from models.private_customers import PrivateCustomer
from models.company_customer import CompanyCustomer
from models.customer_cars import CustomerCar
from models.stores import Store
from models.employees import Employee
from models.orders import Order
from models.order_details import OrderDetail
from models.spare_part_stores import SparePartStore


def main():
    Base.metadata.create_all(engine)
    # order_1 = Order(customer_id=1, employee_id=1, store_id=1)

    # la till back populates på manufacturer
    # lägg till lovetable values i car_models_spare_parts

    # session.add(order_1)
    # session.commit()
    # print(order_1.order_date)

    spareparts = session.query(SparePart).all()

    customers = session.query(Customer).all()

    for customer in customers:
        print(customer)

    for spare in spareparts:
        print(f"{spare.description}".center(30, '='))
        for stores_parts in spare.stores:
            print(stores_parts.store.store_name.ljust(15), end="")
            print(stores_parts.stock_location.ljust(10), end="")
            print(f"{stores_parts.stock}")


if __name__ == "__main__":
    main()
