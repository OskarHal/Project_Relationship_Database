from Data.Models.employees import Employee
from Data.db import session


def get_all_employees():
    return session.query(Employee).all()


def get_employee_by_id(selection):
    return session.query(Employee).filter_by(employee_id=selection).first()

