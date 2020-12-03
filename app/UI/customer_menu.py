from Controllers.customer_controller import get_all_customers, get_customer_by_id
from Data.Models.company_customer import CompanyCustomer
# from Data.Models.customer import Customer
from Data.Models.customer_cars import CustomerCar
from Data.Models.private_customers import PrivateCustomer
import Controllers.customer_controller as cc
from MongoDB.Models.customers import Customer

ERROR_MESSAGE_ONE = "There is no entry in the database "
ERROR_MESSAGE_TWO = " Your type of input is wrong "


def delete_message(success):
    print("Delete successful!".center(30, "-")) if success else print("Delete failed".center(30, "-"))


def edit_data(customer):

    while True:
        print("Edit menu ".center(30, " "))
        print("".center(30, "="))
        print("1.Edit E-mail")
        print("2.Edit Phone number")
        print("0.Exit")

        selection = input("> ")

        if selection == "1":

            edit_email = input("> Enter new email: ")
            cc.edit_new_email(customer, edit_email)

            print(f"The email is now updated to {edit_email}".center(30, " "))
            print("".center(30, "="))

            break

        elif selection == "2":

            edit_phone_number = input("> Enter new phone number: ")
            cc.edit_new_phone_number(customer, edit_phone_number)

            print(f"The phone number is now updated to {edit_phone_number}".center(30, " "))
            print("".center(30, "="))

        elif selection == "0":
            break


def manipulation_data(customer):
    while True:
        print("Select option: ".center(30, " "))
        print("".center(30, "="))
        print("1.Edit")
        print("2.Delete")
        print("3.Show customer car")
        print("4.Show customer order history")
        print("0.Exit")

        selection = input("> ")

        if selection == "1":
            edit_data(customer)
        elif selection == "2":
            print(delete_message(cc.delete_customer(customer)))
            continue
        elif selection == "3":
            pass
        elif selection == "4":
            pass
        elif selection == "0":
            break


def select_customer_menu():

    while True:
        print("Find Customer by:".center(30, " "))
        print("".center(30, "="))
        print("1.ID")
        print("2.First name (Private Customer)")
        print("3.Company name")
        print("0.Exit")
        selection = input("> ")

        if selection == "1":

            selected_id = input("> Enter ID")

            try:
                int(selected_id)
            except ValueError:
                print(ERROR_MESSAGE_TWO + "only enter numbers 0-9")
                continue

            customer = get_customer_by_id(selected_id)

            if customer:
                if customer.customer_type == 1:
                    private_customer = customer.priv_customer
                    print(private_customer)
                    manipulation_data(private_customer)

                elif customer.customer_type == 2:
                    company_customer = customer.comp_customer
                    print(company_customer)
                    manipulation_data(company_customer)

            else:
                print(ERROR_MESSAGE_ONE + "with customer id " + selected_id)

        if selection == "2":

            selected_first_name = input("> Enter First name").lower()
            customer = cc.get_customer_by_first_name(selected_first_name)
            print(customer)
            manipulation_data(customer)
        elif selection == "3":

            selected_company_name = input("> Enter Company name")
            customer = cc.get_customer_by_company_name(selected_company_name)
            print(customer)
            manipulation_data(customer)

        elif selection == "0":
            break


def add_customer_car():
    print("Customer car information".center(30, " "))
    print("".center(30, "="))

    return {f"customer_{i.replace(' ', '_').lower()}": input(f"{i}: ") for i in
            ["Registration nr", "Car brand", "Car model", "Car model_year", "Car color"]}


def verify_information(customer, car):
    print("OBS!".center(30, "-"))
    print("\n".join(f"{key}: {customer[key]}" for key in customer))

    print("car information".center(30, "-"))
    print("\n".join(f"{key}: {car[key]}" for key in car))


def add_private_customer(customer_type, order=False):
    while True:
        print("Private Customer".center(30, " "))
        print("".center(30, "="))

        # ---MYSQL STUFF---
        # priv_customer_dict = {f"private_customer_{i.replace(' ', '_').lower()}": input(f"{i}: ") for i in
        #                       ["First name", "Last name", "Phone", "Email"]}

        priv_customer_dict = {f"customer_{i.replace(' ', '_').lower()}": input(f"{i}: ") for i in
                              ["First name", "Last name", "Phone", "Email"]}

        customer_car_dict = add_customer_car()
        verify_information(priv_customer_dict, customer_car_dict)
        priv_customer_dict.update({"cars": [customer_car_dict]})

        verification = input("Is the information entered correct?\n(1) YES\n(2) NO\n:>  ")

        if verification == "1":
            private_customer = Customer(priv_customer_dict)

            # ---MYSQL STUFF---
            # private_customer = PrivateCustomer(**priv_customer_dict)
            # private_customer.customer = Customer(customer_type=customer_type)
            # private_customer.customer.cars.append(CustomerCar(**customer_car_dict))

            if order:
                return private_customer

            else:
                cc.add_private_customer(private_customer)
                print("Customer saved!".center(30, "-"))
                break

        elif verification == "2":
            print("Save cancelled!".center(30, "-"))
            break

        else:
            print(f"{ERROR_MESSAGE_TWO}. Data wasn't saved!")
            continue


def add_company_customer(customer_type, order=False):
    while True:
        print("Company Customers".center(30, " "))
        print("".center(30, "="))

        comp_customer_dict = {f"company_customer_{i.replace(' ', '_').lower()}": input(f"{i}: ") for i in
                              ["Company Name", "First name", "Last Name", "Email", "Phone"]}

        customer_car_dict = add_customer_car()
        verify_information(comp_customer_dict, customer_car_dict)

        verification = input("Is the information entered correct?\n(1) YES\n(2) NO\n:> ")

        if verification == "1":
            company_customer = CompanyCustomer(**comp_customer_dict)
            company_customer.customer = Customer(customer_type=customer_type)
            company_customer.customer.cars.append(CustomerCar(**customer_car_dict))

            if order:
                return company_customer

            else:
                cc.add_company_customer(company_customer)
                print("Customer saved!".center(30, "-"))
                break

        elif verification == "2":
            print("Save cancelled!".center(30, "-"))
            break

        else:
            print(f"{ERROR_MESSAGE_TWO}. Data wasn't saved!")
            continue


def add_customer_menu():
    while True:
        print("Add Customers Menu".center(30, " "))
        print("".center(30, "="))

        try:
            customer_type = int(input("Enter customer type:\n(1) Private\n(2) Company\n:> "))

        except ValueError:
            print(f"{ERROR_MESSAGE_TWO}")
            continue

        if customer_type == 1:
            add_private_customer(customer_type)
            break

        elif customer_type == 2:
            add_company_customer(customer_type)
            break

        else:
            print(f"Customer type {customer_type} doesn't exist. Choose either 1 or 2")


def customers_menu():
    while True:
        print("Customers Menu".center(30, " "))
        print("".center(30, "="))
        print("1.View All Customers")
        print("2.Select Customer")
        print("3.Add New Customer")
        print("0.Exit")
        selection = input("> ")
        if selection == "1":
            customers = get_all_customers()
            for customer in customers:
                print(customer)
        elif selection == "2":
            select_customer_menu()
        elif selection == "3":
            add_customer_menu()
        elif selection == "0":
            break
