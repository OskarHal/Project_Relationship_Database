import Controllers.employee_controller as ec
from UI.product_menu import input_int_validation


def fire_employee(employee):
    print(f"Give {employee.employee_lastname} reason for being fired".center(30, " "))
    print("=" * 30)
    print("1. The smell is unbearable")
    print("2. Nobody likes him")
    print("3. Your not a fan if Star Wars")

    input_int_validation(message="Thread carefully, your carisma lvl is low!")


def employee_edit_menu(employee):
    while True:
        print("Edit employee menu".center(30, " "))
        print("=" * 30)
        print(f"1. Show orders handled by {employee.employee_lastname}")
        print(f"2. Fire {employee.employee_lastname}")

        selection = input_int_validation(message="Menu selection")

        if selection == 1:
            print(
                ("\n".join(f"Order {count} at {order.order_date}".center(30, " ") +
                           f"\n{details.spare_part.description} \t quantity: {details.quantity}"
                           for count, order in enumerate(employee.orders, 1) for details in order.order_lines))
            )
        elif selection == 2:
            fire_employee(employee)
        elif selection == 0:
            break


def select_employee_menu():
    while True:
        print("Select employee menu".center(30, " "))
        print("=" * 30)
        print("0. Exit")

        selection = input_int_validation(message="Enter employee ID")

        if selection == 0:
            break

        employee = ec.get_employee_by_id(selection)
        employee_edit_menu(employee)
        break


def employee_menu():
    while True:
        print("Employee Menu".center(30, " "))
        print("=" * 30)
        print("1. Show employees")
        print("2. Select employee") # sök namn eller ID
        print("3. Add employee")
        print("0. Exit")

        selection = input_int_validation(message="Menu selection")

        if selection == 1:
            employees = ec.get_all_employees()
            print(
                "\n".join(f"{employee.employee_name} {employee.employee_lastname} works at our office in "
                          f"{employee.store.store_name}" for employee in employees)
            )
        elif selection == 2:
            select_employee_menu()
            break
        elif selection == 3:
            pass # ---> Kör här :D
        elif selection == 0:
            break

