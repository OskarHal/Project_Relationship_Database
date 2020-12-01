from Data.db import Base, engine, session
from Data.Models.manufacturers import Manufacturer
from Data.Models.company_contacts import ManufacturerContact
from Data.Models.suppliers import Supplier
from Data.Models.spare_parts import SparePart
from Data.Models.car_models import CarModel
from Data.Models.customer import Customer
from Data.Models.private_customers import PrivateCustomer
from Data.Models.company_customer import CompanyCustomer
from Data.Models.customer_cars import CustomerCar
from Data.Models.stores import Store
from Data.Models.employees import Employee
from Data.Models.orders import Order
from Data.Models.order_details import OrderDetail
from Data.Models.spare_part_stores import SparePartStore
from UI.main_menu import main_menu
from mysql_to_mongo_migration.migration_functions import fix_suppliers


def main():
    fix_suppliers()
    # Base.metadata.create_all(engine)
    # main_menu()

    # order_1 = Order(customer_id=1, employee_id=1, store_id=1)

    # la till back populates på manufacturer
    # lägg till lovetable values i car_models_spare_parts

    # session.add(order_1)
    # session.commit()
    # print(order_1.order_date)

    # spareparts = session.query(SparePart).all()
    #
    # customers = session.query(Customer).all()
    #
    # orders = session.query(Order).all()
    #
    # for customer in customers:
    #     print(customer)
    #
    # for spare in spareparts:
    #     print(f"{spare.description,spare.manufacturer}".center(30, '='))
    #     for stores_parts in spare.stores:
    #         print(stores_parts.store.store_name.ljust(15), end="")
    #         print(stores_parts.stock_location.ljust(10), end="")
    #         print(f"{stores_parts.stock}")
    #
    # for order in orders:
    #     print(f"{order.order_date}".center(30, '='))

if __name__ == "__main__":
    main()

