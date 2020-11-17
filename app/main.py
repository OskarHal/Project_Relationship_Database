from db import Base, engine
from models.manufacturers import Manufacturer
from models.company_contacts import ManufacturerContact
from models.suppliers import Supplier
from models.spare_parts import SparePart
from models.car_models import CarModel
from models.car_models_spare_parts import car_models_spare_parts
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


if __name__ == "__main__":
    main()
