import Data.Repository.employees_repository as er


def get_all_employees():
    return er.get_all_employees()


def get_employee_by_id(selection):
    return er.get_employee_by_id(selection)

