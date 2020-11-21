from Controllers.customer_controller import get_all_customers, get_customer_by_id
ERROR_MESSAGE_ONE = "There is no entry in the database "
ERROR_MESSAGE_TWO = " Your type of input is wrong "


def manipulation_data(customer):
    while True:
        print("Select what you want to do?")
        print("1.Edit")
        print("2.Delete")
        print("3.Show customer car")
        print("4.Show customer order history")
        print("0.Exit")
        selection = input("> ")
        if selection == "1":
            pass
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
        print("Find Customer by:")
        print("1.ID")
        print("2.First name (Private Customer)")
        print("3.Company name")
        print("4.Registration Number")
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
            pass
        if selection == "3":
            pass
        if selection == "4":
            pass
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










