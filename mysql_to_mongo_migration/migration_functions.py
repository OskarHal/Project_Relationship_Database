from Data.Models.company_customer import CompanyCustomer
from Data.Models.customer import Customer
from Data.Models.customer_cars import CustomerCar
from Data.Models.private_customers import PrivateCustomer
from Data.Models.suppliers import Supplier
from Data.db import session
from MongoDB.Models.suppliers import Supplier as MongoSupplier
from MongoDB.Models.customers import Customers as MongoCustomer


def fix_suppliers():
    suppliers = session.query(Supplier).all()
    for supplier in suppliers:
        as_dict = supplier.__dict__
        del as_dict["_sa_instance_state"]

        mongo_supplier = MongoSupplier(as_dict)
        mongo_supplier.save()


def fix_customers():
    customers = session.query(Customer).all()
    for customer in customers:
        as_dict = customer.__dict__
        if customer.customer_type == 1:
            as_dict.update({'customer_first_name': customer.priv_customer[0].private_customer_first_name})
            as_dict.update({'customer_last_name': customer.priv_customer[0].private_customer_last_name})
            as_dict.update({'customer_phone': customer.priv_customer[0].private_customer_phone})
            as_dict.update({'customer_email': customer.priv_customer[0].private_customer_email})
            del as_dict['priv_customer']
        else:
            as_dict.update({'company_name': customer.comp_customer[0].company_customer_company_name})
            as_dict.update({'customer_first_name': customer.comp_customer[0].company_customer_first_name})
            as_dict.update({'customer_last_name': customer.comp_customer[0].company_customer_last_name})
            as_dict.update({'customer_phone': customer.comp_customer[0].company_customer_phone})
            as_dict.update({'customer_email': customer.comp_customer[0].company_customer_email})
            del as_dict['comp_customer']
        customer_cars = []
        for car in customer.cars:
            customer_cars.append({
                'customer_registration_nr': car.customer_registration_nr,
                'customer_car_brand': car.customer_car_brand,
                'customer_car_model': car.customer_car_model,
                'customer_car_model_year': car.customer_car_model_year,
                'customer_car_color': car.customer_car_color
            })
        as_dict.update({'cars': customer_cars})
        del as_dict['_sa_instance_state']
        del as_dict['customer_type']

        mongo_customer = MongoCustomer(as_dict)
        mongo_customer.save()

