from Data.Models.customer import Customer
from Data.db import session
from Data.Models.private_customers import PrivateCustomer


def get_private_customer():
    return session.query(PrivateCustomer).all()


def get_customer_by_id(selected_id):
    return session.query(Customer).filter_by(customer_id=int(selected_id)).first()


def add_private_customer(customer):
    session.add(customer)
    session.commit()


def get_customer_by_first_name(selected_first_name):
    return session.query(PrivateCustomer).filter_by(private_customer_first_name=selected_first_name).first()


def edit_new_email(customer, edit_email):
    customer.private_customer_email = edit_email
    session.commit()


def edit_new_phone_number(customer, edit_phone_number):
    customer.private_customer_phone = edit_phone_number
    session.commit()