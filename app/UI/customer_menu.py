from Controllers.customer_controller import get_all_customers, get_customer_by_id, get_customer_by_first_name, \
    get_customer_by_company_name, edit_new_email, edit_new_phone_number

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
            edit_new_email(customer, edit_email)
            print("==============")
            print(f"The email is now updated to {edit_email}")
            print("==============")
            break
        if selection == "2":
            edit_phone_number = input("> Enter new phone number: ")
            edit_new_phone_number(customer, edit_phone_number)
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
            customer = get_customer_by_first_name(selected_first_name)
            print(customer)
            manipulation_data(customer)
        if selection == "3":
            selected_company_name = input("> Enter Company name")
            customer = get_customer_by_company_name(selected_company_name)
            print(customer)
            manipulation_data(customer)
        if selection == "0":
            break


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
            pass
        elif selection == "0":
            break










