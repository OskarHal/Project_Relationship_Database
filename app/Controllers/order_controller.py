import Data.Repository.order_repository as ord_repo
from MongoDB.Models.orders import Order
import MongoDB.Repository.order_repository as mongo_repo


def create_order(new_order):
    # #----MySQL----
    # ord_repo.create_order(new_order)
    # for line in new_order.order_lines:
    #     old_stock = ord_repo.get_stock_for_spare_part(line.spare_part_id, new_order.store_id)
    #     if old_stock.stock - line.quantity < 0:
    #         stores = ord_repo.find_different_store(line.spare_part_id, new_order.store_id, line.quantity)
    #         print(f'You can find {old_stock.spare_part.description} in these stores :')
    #         for store in stores:
    #             print(f'{store.store.store_name}, {store.store.store_address}, has {store.stock} in stock')
    #     else:
    #         ord_repo.update_stock(old_stock, line.quantity)

    mongo_repo.create_order(new_order)


def find_order_by_id(order_id) -> Order:
    return ord_repo.find_order_by_id(order_id)


def find_order_by_date(order_date) -> list:
    return mongo_repo.find_order_by_date(order_date)
