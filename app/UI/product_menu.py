from copy import copy
from datetime import date, datetime

from Controllers.product_controller import get_product_by_product_nr, delete_product, \
    get_products_by_product_description_pattern, update_product, add_product
from Data.Models.spare_parts import SparePart



def add_product_interface():
    product_nr = input("Add product nr: ")
    description = input("Add description ")
    purchase_price = float(input("Add purchase price: "))
    selling_price = float(input("Add selling price: "))
    reorder_level = int(input("Add reorder level: "))
    order_quantity = int(input("Add order quantity: "))
    # estimated_time_of_arrival = int(input("Add estimated time of arrival: "))

    manufacturer_id = int(input("Add manufacturer id: "))
    supplier_id = int(input("Add supplier id: "))

    new_product = SparePart(product_nr=product_nr,
                            description=description,
                            purchase_price=purchase_price,
                            selling_price=selling_price,
                            reorder_level=reorder_level,
                            order_quantity=order_quantity,
                            manufacturer_id=manufacturer_id,
                            supplier_id=supplier_id)

    print(new_product)
    add_product(new_product)

def product_menu():
    while True:
        print("Product Menu")
        print("==============")
        print("1. Select product by product number")
        print("2. Search for products by description")
        print("3. Add product")
        print("0. Exit")

        selection = input_int_validation(input_description="")

        if selection == 1:
            product_choice = select_product_by_number()
            if product_choice is not None:
                choose_action_for_product_menu(product_choice)
        elif selection == 2:
            search_products_by_description_pattern()
        elif selection == 3:
            add_product_interface()
        elif selection == 0:
            break

        print("\n")


def select_product_by_number():
    user_input = input_int_validation(input_description="Type product number")
    product = get_product_by_product_nr(str(user_input))

    if product is None:
        print_query_result_message_no_match(category="product nr", user_input=user_input)
    else:
        return product


def choose_action_for_product_menu(product):
    while True:
        print("Select what you want to do?")
        print("1. Show all information")
        print("2. Edit")
        print("3. Delete")
        print("0. Exit")

        selection = input("> ")

        if selection == "1":
            product.print_all_information_with_relationships()
        if selection == "2":
            edit_menu(product)
        if selection == "3":
            print_success_message(delete_product(product))
            product_menu()
        if selection == "0":
            break


def edit_menu(product):
    # choice_dict = {i: value for i, value in enumerate(vars(product).keys())}
    # choice_dict[0] = "Exit"

    print("Edit menu")
    print("==============")
    print("Choose an attribute to edit: ")

    choice_dict = {
        1: "product_nr",
        2: "description",
        3: "purchase_price",
        4: "selling_price",
        5: "reorder_level",
        6: "order_quantity",
        7: "estimated_time_of_arrival",
        0: "Exit"
    }

    while True:
        for key, value in choice_dict.items():
            print(f"{key}. {str(value).capitalize().replace('_', ' ')}")

        menu_selection = input_int_validation(input_description="")

        if menu_selection == 0:
            break
        else:
            edit_product_handler(product=product, attribute_name=choice_dict[menu_selection])

        print("\n")


def edit_product_handler(product: SparePart, attribute_name: str):
    new_value = input_int_validation(input_description="Enter new data: ")
    success = update_product(product=product, attribute_name=attribute_name, new_value=new_value)
    print_success_message(success=success, print_function=product.print_all_information_with_relationships)



def search_products_by_description_pattern():
    user_input = input("Type product description: ")
    products = get_products_by_product_description_pattern(description_pattern=user_input)

    if len(products) < 1:
        print_query_result_message_no_match(category="products", user_input=user_input)
    else:
        for key, product in products.items():
            print(f'{key}. {product}')


def input_int_validation(input_description):
    print(input_description)
    while True:
        try:
            user_input = int(input("> "))
            return user_input
        except ValueError:
            print("You did not write an integer! Try again or type 0 to quit.")


def print_query_result_message_no_match(category, user_input):
    if isinstance(user_input, str):
        print(f"There is no {category} that includes keyword '{user_input}.'")
    elif isinstance(user_input, int):
        print(f"There is no {category} with nr {user_input}.")
    else:
        print(f"No result for {category} with {user_input}.")


def print_success_message(*args, success, print_function=None):
    if success:
        print("Succeeded")

        if print_function is not None:
            print(print_function())

        if len(args) > 0:
            for arg in args:
                print(arg)
    else:
        print("Failed")