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


def update_product(product, attribute, new_value):
    return pr.update_product(product, attribute, new_value)