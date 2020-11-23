from Data.Models.company_customer import CompanyCustomer
from Data.db import session


def get_company_customer():
    return session.query(CompanyCustomer).all()


def get_customer_by_company_name(selected_company_name):
    return session.query(CompanyCustomer).filter_by(company_customer_name=selected_company_name).first()


def edit_new_email(customer, edit_email):
    customer.company_customer_email = edit_email
    session.commit()


def edit_new_phone_number(customer,edit_phone_number):
    customer.company_customer_phone = edit_phone_number
    session.commit()
