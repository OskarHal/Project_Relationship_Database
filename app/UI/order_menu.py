from Controllers.order_controller import create_order, find_order_by_id, find_order_by_date
from UI.customer_menu import *
from Data.Models.orders import Order


def order_id_print(order_id):
    order = find_order_by_id(order_id)
    print("===================")
    if order.customer.customer_type == 1:
        print("test")
        print(f'Order by customer {order.customer.comp_customer[0].company_customer_first_name} '
              f'{order.customer.comp_customer[0].company_customer_last_name},'
              f'employee {order.employees.employee_name} '
              f'in store {order.store.store_name} made on {order.order_date}')
    elif order.customer.customer_type == 2:
        print(f'Order by customer {order.customer.priv_customer[0].private_customer_first_name} '
              f'{order.customer.priv_customer[0].private_customer_last_name}, '
              f'employee {order.employees.employee_name} '
              f'in store {order.store.store_name} made on {order.order_date}')


def order_by_date_print(order_date):
    orders = find_order_by_date(order_date)
    print("===================")
    for order in orders:
        if order.customer.customer_type == 1:
            print(f'Order by customer{order.customer.comp_customer[0].company_customer_first_name} '
                  f'{order.customer.comp_customer[0].company_customer_last_name},'
                  f'employee {order.employees.employee_name} '
                  f'in store {order.store.store_name} made on {order.order_date}')
        elif order.customer.customer_type == 2:
            print(f'Order by customer{order.customer.priv_customer[0].private_customer_first_name} '
                  f'{order.customer.priv_customer[0].private_customer_last_name}, '
                  f'employee {order.employees.employee_name} '
                  f'in store {order.store.store_name} made on {order.order_date}')
    print("")


def get_order_details(customer_id):
    employee_id = int(input("Enter your employee number: "))
    store_id = int(input("Enter your store id"))
    new_order = Order(customer_id=customer_id, employee_id=employee_id, store_id=store_id)
    return new_order


def get_product_in_order(order_id):
    while True:
        product_list = []
        print("what product and how many?")
        product_nr = input("Enter product nr: ")
        quantity = input("Enter how many of said product: ")
        line = [order_id, product_nr, quantity]
        product_list.append(line)
        print(product_list)
        break
    return product_list


"""
Problem med att få ut order_id från den ny skapade ordern, hur tusan skall det lösas?
finns det något bra sätt att få med det med tanke på att den är auto_increment 
så skapas den ju när det läggs in i databasen. 
Går det på något sätt få skapa ordern först, för att få ut senaste order_id't och skicka med den till order_details?

"""


def create_new_order(customer_type):
    if customer_type == "1":
        #customer_id = select_customer_menu()
        new_order = get_order_details(1)
        prod_details = get_product_in_order(new_order.order_id)
        create_order(new_order, prod_details)
    elif customer_type == "2":
        #customer_id = add_customer_menu()
        new_order = get_order_details(1)
        prod_details = get_product_in_order(new_order.order_id)
        create_order(new_order, prod_details)
    else:
        print("No such option exists. Try again")


def order_menu():
    while True:
        print("1. Create order")
        print("2. Find order by id")
        print("3. Find order by date")
        print("0. Exit")
        selection = input("> ")

        if selection == "1":
            print("1. Search for existing customer")
            print("2. Add new Customer")
            selection = input("> ")
            create_new_order(selection)
        elif selection == "2":
            order_id = input("Enter order id: ")
            order_id_print(order_id)
        elif selection == "3":
            order_date = input("Enter order date (yyyy-mm-dd): ")
            order_by_date_print(order_date)
        elif selection == "0":
            break
