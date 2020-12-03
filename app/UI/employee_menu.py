import Controllers.employee_controller as ec
from UI.product_menu import input_int_validation


def fire_message(employee, reason):
    if reason == 1:
        print(f"{employee.employee_lastname} was successfully fired for his terrible smell")

    elif reason == 2:
        print(f"{employee.employee_lastname} was let go because he just couldn't keep his mouth shut")

    elif reason == 3:
        valuables = ec.theft(employee)
        print(
            f"Ouch, looks like you fired {employee.employee_name} {employee.employee_lastname} and he wasn't happy"
            f" with the reason you gave gim. \nHe ran off in your customer {valuables[2]}s"
            f" {valuables[1].customer_car_brand} with {valuables[0][0]} {valuables[0][1]}s from your office in "
            f"{employee.store.store_name}"
        )


def fire_employee(employee):
    while True:
        print(f"Give {employee.employee_lastname} reason for being fired".center(30, " "))
        print("=" * 30)
        print("1. The smell is unbearable")
        print("2. That one time on the company christmas party")
        print("3. Your not a fan if Star Wars")
        print("0. Exit")

        selection = input_int_validation("Thread carefully, your carisma lvl is low!")

        if selection == 1:
            fire_message(employee, selection)
            ec.fire_employee(employee)
            break

        elif selection == 2:
            fire_message(employee, selection)
            ec.fire_employee(employee)
            break

        elif selection == 3:
            fire_message(employee, selection)
            ec.fire_employee(employee)
            break

        elif selection == 0:
            print("Unable")


def employee_edit_menu(employee):
    while True:
        print("Edit employee menu".center(30, " "))
        print("=" * 30)
        print(f"1. Show orders handled by {employee.employee_lastname}")
        print(f"2. Fire {employee.employee_lastname}")
        print("0. Exit")

        selection = input_int_validation("Menu selection")

        if selection == 1:
            # ----MySQL----
            # print(
            #     ("\n".join(f"Order {count} at {order.order_date}".center(30, " ") +
            #                f"\n{details.spare_part.description} \t quantity: {details.quantity}"
            #                for count, order in enumerate(employee.orders, 1) for details in order.order_lines))
            # )
            print("\n".join(f"Order {count} at {order.order_date}".center(30, " ") +
                            f"\n{details['spare_part_id']} \t quantity: {details['quantity']}"
                            for count, order in enumerate(employee.orders, 1) for details in order.order_detail))

        elif selection == 2:
            fire_employee(employee)

        elif selection == 0:
            break


def select_employee_menu():
    while True:
        print("Select employee menu".center(30, " "))
        print("=" * 30)
        print("0. Exit")

        # ----MySQL----
        # selection = input_int_validation("Enter employee ID")

        selection = input("Enter employee first name: ")

        if selection == "0":
            break
        # ----MySQL----
        # employee = ec.get_employee_by_id(selection)
        employee = ec.get_employee_by_first_name(selection)
        if employee is not None:
            employee_edit_menu(employee)
        else:
            print(f"There's no one named {selection} working in our stores")
            continue
        break


def employee_menu():
    while True:
        print("Employee Menu".center(30, " "))
        print("=" * 30)
        print("1. Show employees")
        print("2. Select employee")
        print("3. Add employee")
        print("0. Exit")

        selection = input_int_validation("Menu selection")

        if selection == 1:
            employees = ec.get_all_employees()
            print(
                "\n".join(f"{i}. {employee.employee_name} {employee.employee_lastname} works at our office in "
                          f"{employee.store.store_name}" for i, employee in enumerate(employees, 1))
            )

        elif selection == 2:
            select_employee_menu()
            break

        elif selection == 3:
            pass

        elif selection == 0:
            break

