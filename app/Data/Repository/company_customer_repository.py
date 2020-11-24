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


def get_customer_by_company_name(selected_company_name):
    return session.query(CompanyCustomer).filter_by(company_customer_company_name=selected_company_name).first()


def edit_new_email(customer, edit_email):
    customer.company_customer_email = edit_email
    session.commit()


def edit_new_phone_number(customer, edit_phone_number):
    customer.company_customer_phone = edit_phone_number

