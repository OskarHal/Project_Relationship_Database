from Data.Models.customer_cars import CustomerCar
from Data.db import session
import random


def steal_car():
    customer_cars = session.query(CustomerCar.customer_registration_nr).all()

    stolen_car = session.query(CustomerCar).filter_by(customer_registration_nr=random.choice(customer_cars)[0]).first()

    session.query(CustomerCar).filter_by(customer_registration_nr=stolen_car.customer_registration_nr).delete()

    return stolen_car
