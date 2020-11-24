import os

from Controllers.product_controller import get_product_by_product_nr, delete_product, \
    get_products_by_product_description_pattern, update_product, add_product, \
    get_manufacturer_by_id, get_supplier_by_id, get_all_car_models

from Data.Models.spare_part_stores import SparePartStore
from Data.Models.spare_parts import SparePart


def add_existing_car_models():
    chosen_car_models = []
    available_car_models = get_all_car_models()
    available_car_models_id = []

    while True:
        print(f"Possible car models to add".center(50, "-"))
        for car_model in available_car_models:
            print(car_model)
            available_car_models_id.append(car_model.car_model_id)

        chosen_car_model_id = input_int_validation("car model id: ")
        car_model = [cm for cm in available_car_models if cm.car_model_id == chosen_car_model_id]

        if not car_model:
            print("There are no car models to choose from with that id!")
            continue
        else:
            car_model = car_model[0]
            chosen_car_models.append(car_model)
            available_car_models.remove(car_model)

        if not available_car_models:
            print("no more car models to add")
            break

        if user_question_add_more("Want to add more car models?"):
            break

        print(f"Added cars".center(50, "-"))
        [print(f"{car_model}") for car_model in chosen_car_models]
        print("\n")

    return chosen_car_models


def add_manufacturer():
    return get_manufacturer_by_id(manufacturer_id=input_int_validation("manufacturer id: "))


def add_supplier():
    return get_supplier_by_id(supplier_id=input_int_validation("Supplier id: "))


def add_spare_part_stores():
    new_spare_part_stores = []

    while True:
        new_spare_part_store_dict = {f"{i.replace(' ', '_').lower()}": input(f"{i}: ") for i in
                                     ["Stock", "Stock location", "Store id"]}

        new_spare_part_stores.append(SparePartStore(**new_spare_part_store_dict))

        answer = input("Want to add product to more stores? (yes or no): ").lower()
        if answer == "no":
            break

    return new_spare_part_stores


def add_product_interface():
    add_product_dict = {f"{i.replace(' ', '_').lower()}": input(f"{i}: ") for i in
                        [
                            "Product nr",
                            "Description",
                            "Purchase price",
                            "Selling price",
                            "Reorder level",
                            "Order quantity",
                            "Estimated time of arrival"
                        ]}

    new_product = SparePart(**add_product_dict)
    new_product.manufacturer, new_product.supplier = add_manufacturer(), add_supplier()
    [new_product.car_models.append(car_model) for car_model in add_existing_car_models()]
    [new_product.stores.append(store) for store in add_spare_part_stores()]

    if add_product(new_product):
        print(f"You successfully added a product to the database!".center(45, "-"))
        print(new_product.print_all_information_with_relationships())
        os.system("pause")
    else:
        print("Something went wrong")
        os.system("pause")


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
    choice_dict = {i: value for i, value in enumerate(vars(product).keys()) if i != 0}
    choice_dict[0] = "Exit"

    while True:
        print("Edit menu")
        print("==============")
        print("Choose an attribute to edit: ")

        for key, value in choice_dict.items():
            print(f"{key}. {str(value).capitalize().replace('_', ' ')}")

        menu_selection = input_int_validation(input_description="")

        if menu_selection == 0:
            break
        elif menu_selection > 10:
            print("choose a number between 1-10")
            os.system("pause")
            continue

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
    while True:
        try:
            user_input = int(input(f"{input_description}: "))
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


def user_question_add_more(message):
    magic_number = 0
    while True:
        answer = input(f"{message} (yes or no): ").lower()
        if answer == "no":
            return True
        elif answer == "yes":
            return False
        else:
            print("Sorry, I did not understand that!")
            magic_number += 1
            if magic_number == 3:
                print("MARRY CRISTMAS!")
                os.system("notepad marry_christmas_wish_list.txt")
