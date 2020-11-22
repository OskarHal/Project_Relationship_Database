import Data.Repository.order_repository as ord_repo


def create_order(new_order, prod_details):
    ord_repo.create_order(new_order, prod_details)


def find_order_by_id(order_id):
    return ord_repo.find_order_by_id(order_id)


def find_order_by_date(order_date):
    return ord_repo.find_order_by_date(order_date)
