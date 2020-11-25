import Data.Repository.employees_repository as er
import Data.Repository.customer_cars_repository as ccr


def get_all_employees():
    return er.get_all_employees()


def get_employee_by_id(selection):
    return er.get_employee_by_id(selection)


def fire_employee(employee):
    return er.fire_employee(employee)


def theft(thief):
    valuables = [er.steal_products(thief), ccr.steal_car()]

    if valuables[1].owner.customer_type == 1:
        valuables.append(valuables[1].owner.priv_customer[0].private_customer_first_name)

    elif valuables[1].owner.customer_type == 2:
        valuables.append(valuables[1].owner.comp_customer[0].company_customer_company_name)

    return valuables
