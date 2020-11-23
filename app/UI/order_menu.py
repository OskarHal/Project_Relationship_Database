from Controllers.order_controller import create_order, find_order_by_id, find_order_by_date
from Controllers.product_controller import get_all_products
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


def get_order_details(existing=False):
    print("===================")
    employee_id = int(input("Enter your employee number: "))
    store_id = int(input("Enter your store id"))

    if existing:
        customer_id = input("Enter customer_id: ")
        new_order = Order(customer_id=customer_id, employee_id=employee_id, store_id=store_id)
        return new_order
    else:
        new_order = Order(employee_id=employee_id, store_id=store_id)
        return new_order


#lägga till flera produkter
def get_product_in_order(new_order):
    print(f"Products".center(45, '#'))
    products = get_all_products()
    for product in products:
        #print(f'Product ID: {product.spare_part_id}, Description: {product.description}')
        print(f"Id: ".ljust(30), end='|')
        print(f"{product.spare_part_id}")
        print(f"Description: ".ljust(30), end='|')
        print(f"{product.description}")
        print(f"".center(45, '-'))
    print()
    while True:
        print("What product id? Enter 'done' to complete the order.")
        spare_part_id = input("Enter product id: ")
        if spare_part_id.lower() == "done":
            break
        quantity = input("How many of said product: ")
        line = OrderDetail(spare_part_id=spare_part_id, quantity=quantity)
        new_order.order_lines.append(line)
    return new_order


def create_new_order(customer_type):
    if customer_type == "1":
        new_order = get_order_details(existing=True)
        get_product_in_order(new_order)
        create_order(new_order)
    elif customer_type == "2":
        new_order = get_order_details()
        customer = add_private_customer(1, order=True)
        new_order.customer = customer.customer
        get_product_in_order(new_order)
        create_order(new_order)
    elif customer_type == "3":
        new_order = get_order_details()
        customer = add_company_customer(2, order=True)
        new_order.customer = customer.customer
        get_product_in_order(new_order)
        create_order(new_order)
    else:
        print("No such option exists. Try again")


def order_menu():
    while True:
        print("===================")
        print("1. Create order")
        print("2. Find order by id")
        print("3. Find order by date")
        print("0. Exit")
        selection = input("> ")
        print()
        if selection == "1":
            print("1. Use existing customer")
            print("2. Add new Private Customer")
            print("3. Add new Company Customer")
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
