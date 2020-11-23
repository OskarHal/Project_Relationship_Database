import Data.Repository.company_customer_repository as ccr
import Data.Repository.private_customer_repository as pcr


def get_all_customers():
    company_customer = ccr.get_company_customer()
    private_customer = pcr.get_private_customer()
    return company_customer+private_customer


def get_customer_by_id(selected_id):
    return pcr.get_customer_by_id(selected_id)


def get_customer_by_first_name(selected_first_name):
    return pcr.get_customer_by_first_name(selected_first_name)


def get_customer_by_company_name(selected_company_name):
    return ccr.get_customer_by_company_name(selected_company_name)


def edit_new_email(customer, edit_email):
    if customer.customer.customer_type == 1:
        pcr.edit_new_email(customer, edit_email)
    else:
        ccr.edit_new_email(customer, edit_email)


def edit_new_phone_number(customer, edit_phone_number):
    if customer.customer.customer_type == "1":
        pcr.edit_new_phone_number(customer, edit_phone_number)
    else:
        ccr.edit_new_phone_number(customer, edit_phone_number)


def add_private_customer(customer):
    pcr.add_private_customer(customer)


def add_company_customer(customer):
    ccr.add_company_customer(customer)

