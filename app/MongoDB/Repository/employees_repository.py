from MongoDB.Models.employees import Employee
from MongoDB.Models.spare_parts import SparePart
import random


def get_all_employees():
    return Employee.all()


def get_employee_by_first_name(selection):
    return Employee.find(employee_first_name=selection.title()).first_or_none()


def steal_products(thief):
    available_items = SparePart.find(**{"stores.store_id": thief.store_id})
    stolen_item = random.choice(available_items)
    amount = stolen_item.stores[0]["stock"]
    stolen_item.stores[0]["stock"] = 0
    stolen_item.save()
    return amount, stolen_item


def fire_employee(employee):
    Employee.delete(_id=employee._id)


def save_employee(employee_dict):
    employee = Employee(employee_dict)
    employee.save()
    return employee
