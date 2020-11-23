from Controllers.product_controller import get_product_by_product_nr, delete_product, \
    get_products_by_product_description_pattern, update_product
from Data.Models.spare_parts import SparePart


def edit_menu(product):
    choice_dict = {
        1: "product_nr",
        2: "description",
        3: "purchase_price",
        4: "selling_price",
        5: "reorder_level",
        6: "order_quantity",
        7: "estimated_time_of_arrival",
        8: "manufacturer_id"
    }

     # for {i + 1: product_attribute for i in enumerate(vars(product).keys())}:

    #   choice_dict[product_attribute] =

    while True:
        for key, value in choice_dict.items():
            print(f"{key}. {str(value).capitalize().replace('_', ' ')}")

        menu_selection = int(input("> "))

        if menu_selection == 0:
            break

        new_value = input("> Enter new data: ")

        if update_product(product=product, attribute_name=choice_dict[menu_selection], new_value=new_value):
            print("Changes succeeded")
            print(product.print_all_information_with_relationships())
        else:
            print("Failed")

        print("\n")


def product_menu():
    while True:
        print("Product Menu")
        print("==============")
        print("1. Select product by product number")
        print("2. Search for products by description")
        print("3. Add product")
        print("0.Exit")

        selection = input("> ")

        if selection == "1":
            product_choice = select_product_by_number()
            if product_choice is not None:
                choose_action_for_product_menu(product_choice)

        elif selection == "2":
            search_products_by_description_pattern()

        elif selection == "3":
            pass
        elif selection == "0":
            break

        print("\n")


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
            print_delete_message(delete_product(product))
            product_menu()
        if selection == "0":
            break


def edit_product(product: SparePart):
    pass


def add_product(product: SparePart):
    pass


def select_product_by_number():
    user_input = input_int_validation(message="Type product number")
    product = get_product_by_product_nr(str(user_input))

    if product is None:
        print_result_message_no_match_nr(category="product", user_input=user_input)
    else:
        return product


def search_products_by_description_pattern():
    user_input = input("Type product description: ")
    products = get_products_by_product_description_pattern(description_pattern=user_input)

    if len(products) < 1:
        print_result_message_no_match_nr(category="products", user_input=user_input)
    else:
        for key, product in products.items():
            print(f'{key}. {product}')


def input_int_validation(message):
    while True:
        try:
            user_input = int(input(f"{message}:\n>"))
            return user_input
        except ValueError:
            print("You did not write an integer! Try again or type 0 to quit.")


def print_result_message_no_match_str(category, user_input):
    print(f"There is no {category} that includes keyword '{user_input}'")


def print_result_message_no_match_nr(category, user_input):
    print(f"There is no {category} with nr {user_input}")


def print_delete_message(success):
    print("Delete succeeded") if success else print("Delete failed")
