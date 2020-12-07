import Data.Repository.employees_repository as er
import Data.Repository.customer_cars_repository as ccr
import MongoDB.Repository.employees_repository as mer
import MongoDB.Repository.customers_repository as mcr


def get_all_employees():
    return mer.get_all_employees()
    # ----MySQL----
    # return er.get_all_employees()


def get_employee_by_id(selection):
    return er.get_employee_by_id(selection)


def fire_employee(employee):
    return mer.fire_employee(employee)
    # ---MySQL---
    # return er.fire_employee(employee)


def theft(thief):
    amount, stolen_item = mer.steal_products(thief)
    customer = mcr.steal_car()
    # ---MySQL---
    # if valuables[1].owner.customer_type == 1:
    #     valuables.append(valuables[1].owner.priv_customer[0].private_customer_first_name)
    #
    # elif valuables[1].owner.customer_type == 2:
    #     valuables.append(valuables[1].owner.comp_customer[0].company_customer_company_name)

    return amount, stolen_item, customer


def get_employee_by_first_name(selection):
    return mer.get_employee_by_first_name(selection)


def save_employee(employee_dict):
    return mer.save_employee(employee_dict)
