from Data.db import session
from Data.Models.orders import Order


def create_order(new_order):
    try:
        session.add(new_order)
        session.commit()
    except:
        session.rollback()


def find_order_by_id(order_id):
    return session.query(Order).filter(Order.order_id == order_id).first()


def find_order_by_date(order_date):
    return session.query(Order).filter(Order.order_date.like(f'%{order_date}%')).all()
