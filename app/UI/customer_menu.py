from Controllers.customer_controller import get_all_customers, get_customer_by_id
from Data.Models.company_customer import CompanyCustomer
from Data.Models.customer import Customer
from Data.Models.private_customers import PrivateCustomer
import Controllers.customer_controller as cc


ERROR_MESSAGE_ONE = "There is no entry in the database "
ERROR_MESSAGE_TWO = " Your type of input is wrong "


def edit_data(customer):
    while True:
        print("Choose the edit")
        print("==============")
        print("1.Edit E-mail")
        print("2.Edit Phone number")
        print("0.Exit")
        selection = input("> ")
        if selection == "1":
            edit_email = input("> Enter new email: ")
            cc.edit_new_email(customer, edit_email)
            print("==============")
            print(f"The email is now updated to {edit_email}")
            print("==============")
            break
        if selection == "2":
            edit_phone_number = input("> Enter new phone number: ")
            cc.edit_new_phone_number(customer, edit_phone_number)
            print("==============")
            print(f"The phone number is now updated to {edit_phone_number}")
            print("==============")
        if selection == "0":
            break

def manipulation_data(customer):
    while True:
        print("Edit menu")
        print("==============")
        print("Select what you want to do?")
        print("1.Edit")
        print("2.Delete")
        print("3.Show customer car")
        print("4.Show customer order history")
        print("0.Exit")
        selection = input("> ")
        if selection == "1":
            edit_data(customer)
        if selection == "2":
            pass
        if selection == "3":
            pass
        if selection == "4":
            pass
        if selection == "0":
            break


def select_customer_menu():
    while True:
        print("Customers Menu")
        print("==============")
        print("Find Customer by:")
        print("==============")
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
                    private_customer = customer.priv_customer[0]
                    print(private_customer)
                    manipulation_data(private_customer)

                elif customer.customer_type == 2:
                    company_customer = customer.comp_customer[0]
                    print(company_customer)
                    manipulation_data(company_customer)

            else:
                print(ERROR_MESSAGE_ONE + "with customer id " + selected_id)
        if selection == "2":
            selected_first_name = input("> Enter First name").lower()
            customer = cc.get_customer_by_first_name(selected_first_name)
            print(customer)
            manipulation_data(customer)
        if selection == "3":
            selected_company_name = input("> Enter Company name")
            customer = cc.get_customer_by_company_name(selected_company_name)
            print(customer)
            manipulation_data(customer)
        if selection == "0":
            break


def add_private_customer(customer_type, order=False):
    while True:
        print("Private Customer".center(30, " "))
        print("".center(30, "="))

        priv_customer_dict = {f"private_customer_{i.replace(' ', '_').lower()}": input(f"{i}: ") for i in ["First name", "Last name", "Phone", "Email"]}

        print("OBS!".center(30, "-"))
        print("\n".join(f"{key}: {priv_customer_dict[key]}" for key in priv_customer_dict))

        verification = input("Is the information entered correct?\n(1) YES\n(2) NO\n:>")

        if verification == "1":
            private_customer = PrivateCustomer(**priv_customer_dict)
            private_customer.customer = Customer(customer_type=customer_type)
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

        comp_customer_dict = {f"company_customer_{i.replace(' ', '_').lower()}": input(f"{i}: ") for i in ["Company Name", "Contact first name", "Contact last Name", "Email", "Phone"]}

        print("OBS!".center(30, "-"))
        print("\n".join(f"{key}: {comp_customer_dict[key]}" for key in comp_customer_dict))

        verification = input("Is the information entered correct?\n(1) YES\n(2) NO\n:> ")

        if verification == "1":
            company_customer = CompanyCustomer(**comp_customer_dict)
            company_customer.customer = Customer(customer_type=customer_type)
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
        elif customer_type == 2:
            add_company_customer(customer_type)
        else:
            print(f"Customer type {customer_type} doesn't exist. Choose either 1 or 2")


def customers_menu():
    while True:
        print("Customers Menu")
        print("==============")
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
