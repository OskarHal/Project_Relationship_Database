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


def delete_customer(customer):
    success = False
    try:
        session.query(Customer).filter(Customer.customer_id == customer[0].customer_id).delete()
        session.commit()
        success = True
    except:
        session.rollback()
    finally:
        return success
