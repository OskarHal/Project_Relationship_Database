from UI.customer_menu import customers_menu
from UI.product_menu import product_menu
from UI.order_menu import order_menu



def main_menu():
    while True:
        print("Main Menu")
        print("=========")
        print("1. Customers")
        print("2. Products")
        print("3. Orders")
        print("0. Quit")

        selection = input("> ")
        if selection == "1":
            customers_menu()
        elif selection == "2":
            product_menu()
        elif selection == "3":
            order_menu()
        elif selection == "0":
            break
