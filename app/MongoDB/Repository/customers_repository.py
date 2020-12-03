from MongoDB.Models.customers import Customer


def add_customer(customer: Customer):
    customer.save()


def get_customer_by_company_name(selected_company_name):
    return Customer.find(company_name=selected_company_name).first_or_none()
    #return session.query(CompanyCustomer).filter_by(company_customer_company_name=selected_company_name).first()


def delete_customer(customer):
    customer.delete(_id=customer._id)
    return True


def get_customer_by_first_name(selected_first_name):
    return Customer.find(customer_first_name=selected_first_name).first_or_none()

