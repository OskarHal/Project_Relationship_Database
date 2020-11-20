from Data.db import session
from Data.Models.private_customers import PrivateCustomer


def get_private_customer():
    return session.query(PrivateCustomer).all()

def  get_customer_by_id():
    return session.query()