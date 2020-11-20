from Controllers.customer_controller \
import get_all_customers, add_new_company_customer





def select_customer_menu():
    while True:
        print("Find Customer by:")
        print("1.ID")
        print("2.First name (Private Customer)")
        print("3.Company name")
        print("0.Exit")
        selection = input("> ")
        if selection == "1":
            selected_id = input("> Enter ID")
            get_customer_by_id()

        if selection == "2":
            pass
        if selection == "3":
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










