from MongoDB.Models.customers import Customer


def add_customer(customer: Customer):
    customer.save()
