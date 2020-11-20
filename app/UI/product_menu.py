from Controllers.product_controller import get_all_products, get_product_by_product_nr
from Data.Models.spare_parts import SparePart
from Data.Repository.products_repository import get_product_by_product_description


def select_product_menu():
    while True:
        print("select product by: ")
        print("1. Product number")
        print("2. Name")
        print("0.Exit")

        selection = input("> ")

        if selection == "1":
            product_nr = input("Type product number")
            product = get_product_by_product_nr(product_nr)

            print(f"Product number {product.product_nr}".center(30, '#'))
            print('Category'.ljust(30), end="")
            print("Information")
            print((30 + len("Information")) * "-")
            print(f"Description: ".ljust(30), end='')
            print(f"{product.description}")
            print(f"Purchase price ".ljust(30), end='')
            print(f"{product.purchase_price}")
            print(f"Selling price".ljust(30), end='')
            print(f"{product.selling_price}")
            print(f"Reorder lever".ljust(30), end='')
            print(f"{product.reorder_level}")
            print(f"Order quantity".ljust(30), end='')
            print(f"{product.order_quantity}")
            print(f"Estimated time of arrival".ljust(30), end='')
            print(f"{product.estimated_time_of_arrival}")
            print(f"manufacturer").ljust(30), end='')







        elif selection == "2":
            description = input("Type product description: ")
            products = get_product_by_product_description(description_pattern=description)
            for product in products:
                print(product)
        elif selection == "0":
            break


def product_menu():
    while True:
        print("Product Menu")
        print("==============")
        print("1. Select product")
        print("0.Exit")
        selection = input("> ")
        if selection == "1":
            select_product_menu()
