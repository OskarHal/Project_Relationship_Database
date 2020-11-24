import Data.Repository.employees_repository as er
import Data.Repository.customer_cars_repository as ccr


def get_all_employees():
    return er.get_all_employees()


def get_employee_by_id(selection):
    return er.get_employee_by_id(selection)


def fire_employee(employee):
    return er.fire_employee(employee)


def theft(thief):
    amount, item = er.steal_products(thief)
    car = ccr.steal_car()
    if car.owner.customer_type == 1:
        owner = car.owner.priv_customer[0].private_customer_first_name
    elif car.owner.customer_type == 2:
        owner = car.owner.comp_customer[0].company_customer_company_name
    return car, amount, item, owner
