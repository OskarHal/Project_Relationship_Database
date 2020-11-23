from Data.Models.company_customer import CompanyCustomer
from Data.Models.customer import Customer
from Data.db import session


def get_company_customer():
    return session.query(CompanyCustomer).all()


def add_company_customer(customer):
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
