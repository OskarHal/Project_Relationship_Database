from Data.Repository import products_repository as pr


def get_all_products():
    return pr.get_all_products()