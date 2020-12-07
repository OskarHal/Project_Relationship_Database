from MongoDB.Models.customers import Customer
import random


def add_customer(customer: Customer):
    customer.save()


def steal_car():
    customer_cars = Customer.all()

    stolen_car = random.choice(customer_cars)

    grand_theft_auto = Customer.find(_id=stolen_car._id).first_or_none()
    grand_theft_auto.delete_field("cars")

    return stolen_car
