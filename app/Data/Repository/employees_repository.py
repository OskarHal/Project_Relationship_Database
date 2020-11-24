from Data.Models.employees import Employee
from Data.Models.spare_part_stores import SparePartStore
from Data.db import session
import random


def get_all_employees():
    return session.query(Employee).all()


def get_employee_by_id(selection):
    return session.query(Employee).filter_by(employee_id=selection).first()


def fire_employee(employee):
    try:
        session.query(Employee).filter_by(employee_id=employee.employee_id).delete()
        session.commit()
    except:
        session.rollback()


def steal_products(thief):
    item = session.query(SparePartStore).filter(SparePartStore.store_id == thief.store_id) \
        .filter(SparePartStore.spare_part_id == random.choice([1, 2, 3, 4])).first()
    amount = item.stock
    item.stock = 0
    session.commit()
    return amount, item.spare_part.description
