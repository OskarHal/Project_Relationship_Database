from MongoDB.Models.employees import Employee


def get_all_employees():
    return Employee.all()


def get_employee_by_first_name(selection):
    return Employee.find(employee_name=selection.capitalize()).first_or_none()
