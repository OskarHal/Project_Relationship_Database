from Controllers.product_controller import get_all_products
from Data.Models.spare_parts import SparePart


def products_menu():
    while True:
        print("Products Menu")
        print("==============")
        print("1.get all products")
        print("0.Exit")
        selection = input("> ")

        if selection == "1":
            spare_parts = get_all_products()

            for spare_part in spare_parts:
                print(spare_part)





