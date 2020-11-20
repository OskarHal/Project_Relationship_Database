from Data.Repository import products_repository as pr


def get_all_products():
    return pr.get_all_products()


def get_product_by_product_nr(product_nr: str):
    return pr.get_product_by_product_nr(product_nr)


def product_by_product_description(description_pattern):
    products = pr.get_product_by_product_description(description_pattern)
    return {i + 1: products for i, products in enumerate(products)}
