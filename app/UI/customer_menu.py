from Controllers.customer_controller \
import get_all_customers, add_new_company_customer


def edit_company_customer_menu():
    pass


def delete_company_customer_menu():
    pass


def company_customer_menu():
    while True:
        print("1.View Customer")
        print("2.Edit Customer")
        print("3.Delete Customer")
        print("4.Add New Customer")
        print("0.Exit")

        selection = input("> ")
        if selection == "1":
            customers = get_all_customers(1)
            #for customer in customers:
                #print(customer)
            pass
        elif selection == "2":
            edit_company_customer_menu()
        elif selection == "3":
            delete_company_customer_menu()
        elif selection == "4":
            add_new_company_customer()
        elif selection == "0":
            break


def customers_menu():
    while True:
        print("Customers Menu")
        print("==============")
        print("1.Company Customer")
        print("2.Private Company")
        print("0.Exit")
        selection = input("> ")

        if selection == "1":
            company_customer_menu()

        elif selection == "2":
            pass
        elif selection == "0":
            break










