from Data.Models.customer import Customer
from Data.db import session
from Data.Models.private_customers import PrivateCustomer


def get_private_customer():
    return session.query(PrivateCustomer).all()


def get_customer_by_id(selected_id):
    return session.query(Customer).filter_by(customer_id=int(selected_id)).first()


def add_private_customer(customer):
    return PrivateCustomer(**customer)