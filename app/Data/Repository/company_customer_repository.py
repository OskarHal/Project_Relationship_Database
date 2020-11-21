from Data.Models.company_customer import CompanyCustomer
from Data.db import session


def get_company_customer():
    return session.query(CompanyCustomer).all()

