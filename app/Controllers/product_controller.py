from Data.Models.spare_parts import SparePart
from Data.Repository import products_repository as pr


def get_all_products() -> list:
    return pr.get_all_products()


def get_product_by_product_nr(product_nr: str) -> SparePart:
    return pr.get_product_by_product_nr(product_nr)


def get_products_by_product_description_pattern(description_pattern: str) -> {}:
    products = pr.get_products_by_product_description_pattern(description_pattern)
    return {i + 1: products for i, products in enumerate(products)}


def delete_product(product) -> bool:
    return pr.delete_product(product)


def update_product(product, attribute_name, new_value):
    return pr.update_product(product=product, attribute_name=attribute_name, new_value=new_value)

def add_product(product):
    return pr.add_product(product)


def get_all_stores():
    return pr.get_all_stores()

def get_car_model_by_id(car_model_id):
    return pr.get_car_model_by_id(car_model_id=car_model_id)

def get_manufacturer_by_id(manufacturer_id):
    return pr.get_manufacturer_by_id(manufacturer_id=manufacturer_id)

def get_supplier_by_id(supplier_id):
    return pr.get_supplier_by_id(supplier_id=supplier_id)

# def add_spare_part_store(store_id, stock_location, stock):
#    pr.add_spare_part_store(stock_id=store_id, stock_location=stock_location, stock=stock)

def get_all_car_models():
    return pr.get_all_car_models()