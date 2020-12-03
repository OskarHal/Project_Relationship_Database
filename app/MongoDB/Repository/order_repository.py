from MongoDB.Models.orders import Order


def create_order(new_order):
    new_order.save()


def find_order_by_date(order_date):
    #return Order.find(**{'order_date': / ^ order_date / i})
    #{"$gte": new Date("2019-05-02"), "$lt": newDate("2019-05-18")}})
    #(stock = {'$gt': 1800})
    #"OrderDate": {"$gt": {"$date": "order_date"}}
    # prods = Product.find(**{'name': 'Ball'})
    #: / ^ order_date / i})
    #return Order.find({'order_date':/^order_date/i})
    return Order.find(order_date=order_date)
    #----MySQL----
    #return session.query(Order).filter(Order.order_date.like(f'%{order_date}%')).all()
