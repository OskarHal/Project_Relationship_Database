from MongoDB.Models.orders import Order


def create_order(new_order):
    for order in new_order.order_detail:
        del order['spare_part']
    new_order.save()


def find_order_by_date(order_date):
    return Order.find(order_date=order_date)
