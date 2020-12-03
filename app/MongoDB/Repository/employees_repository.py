from MongoDB.Models.employees import Employee
from MongoDB.Models.spare_parts import SparePart
import random

def get_all_employees():
    return Employee.all()


def get_employee_by_first_name(selection):
    return Employee.find(employee_name=selection.capitalize()).first_or_none()


def steal_products(thief):
    available_items = SparePart.find_embedded("stores.store_id", thief.store_id)
    stolen_item = random.choice(available_items)
    print(stolen_item.stores[0]["stock"])
    amount = stolen_item.stores[0]["stock"]
    stolen_item.stores[0]["stock"] = 0
    stolen_item.save()
    return amount, stolen_item


# def steal_products(thief):
#     item = session.query(SparePartStore).filter(SparePartStore.store_id == thief.store_id) \
#         .filter(SparePartStore.spare_part_id == random.choice([1, 2, 3, 4])).first()
#     amount = item.stock
#     item.stock = 0
#     session.commit()
#     return amount, item.spare_part.description
