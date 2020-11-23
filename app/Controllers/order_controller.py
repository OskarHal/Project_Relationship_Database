import Data.Repository.order_repository as ord_repo
from Data.Models.orders import Order


def create_order(new_order):
    ord_repo.create_order(new_order)


def find_order_by_id(order_id) -> Order:
    return ord_repo.find_order_by_id(order_id)


def find_order_by_date(order_date) -> list:
    return ord_repo.find_order_by_date(order_date)
