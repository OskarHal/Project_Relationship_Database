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
from mysql_to_mongo_migration.migration_functions import fix_suppliers, fix_customers, fix_stores, fix_employees


def main():
    # fix_customers()
    # fix_suppliers()
    # fix_employees()
    # fix_stores()
    # Base.metadata.create_all(engine)
    # main_menu()


if __name__ == "__main__":
    main()

