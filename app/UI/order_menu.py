from Controllers.order_controller import create_order, find_order_by_id, find_order_by_date
from UI.customer_menu import *
from Data.Models.orders import Order
from Data.Models.order_details import OrderDetail


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


def get_product_in_order(new_order):
    while True:
        print("what product and how many?")
        sparepart_id = input("Enter product nr: ")
        quantity = input("Enter how many of said product: ")
        line = OrderDetail(spare_part_id=sparepart_id, quantity=quantity)
        new_order.order_lines.append(line)
        print(new_order)
        break
    return new_order


def create_new_order(customer_type):
    if customer_type == "1":
        #customer_id = select_customer_menu()
        new_order = get_order_details(1)
        get_product_in_order(new_order)
        create_order(new_order)
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
