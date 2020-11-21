from Controllers.product_controller import get_all_products, get_product_by_product_nr
from Data.Models.spare_parts import SparePart
from Data.Repository.products_repository import get_product_by_product_description


def select_product_menu():
    while True:
        print("Select product by: ")
        print("1. Product number")
        print("2. Name")
        print("0.Exit")

        selection = input("> ")

        if selection == "1":
            product_nr = input("Type product number:\n>")
            product = get_product_by_product_nr(product_nr)
            
            if product is None:
                print("No product with that number:\n>")
                continue

            print(f"Product number {product.product_nr}".center(45, '#'))
            print((30 + len("Information")) * "-")
            print('Category'.ljust(30), end="|")
            print("Information")
            print((30 + len("Information")) * "-")
            print(f"Description: ".ljust(30), end='|')
            print(f"{product.description}")
            print(f"Purchase price ".ljust(30), end='|')
            print(f"{product.purchase_price}")
            print(f"Selling price".ljust(30), end='|')
            print(f"{product.selling_price}")
            print(f"Reorder level".ljust(30), end='|')
            print(f"{product.reorder_level}")
            print(f"Order quantity".ljust(30), end='|')
            print(f"{product.order_quantity}")
            print(f"Estimated time of arrival".ljust(30), end='|')
            print(f"{product.estimated_time_of_arrival}")
            print(f"Manufacturer".ljust(30), end='|')
            print(f"{product.manufacturer.manufacturer_name}")
            print(f"Supplier".ljust(30), end='|')
            print(f"{product.supplier.supplier_name}")
            print((30 + len("Information")) * "-")
            print("Availability".center(60))
            print((60 + len("Availability")) * "-")
            print('Store'.ljust(30), end="")
            print("Store location".ljust(30), end="")
            print("Stock")
            print((60 + len("Availability")) * "-")

            for stores_parts in product.stores:
                print(stores_parts.store.store_name.ljust(30), end="")
                print(stores_parts.stock_location.ljust(30), end="")
                print(f"{stores_parts.stock} items")

        elif selection == "2":
            description = input("Type product description: ")
            products = get_product_by_product_description(description_pattern=description)
            for product in products:
                print(product)
        elif selection == "0":
            break

        print("\n")


def product_menu():
    while True:
        print("Product Menu")
        print("==============")
        print("1. Select product")
        print("0.Exit")
        selection = input("> ")
        if selection == "1":
            select_product_menu()
