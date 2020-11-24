from Data.db import session
from Data.Models.orders import Order
from Data.Models.spare_part_stores import SparePartStore


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


def get_stock_for_spare_part(spare_part_id, store_id):
    return session.query(SparePartStore).filter(SparePartStore.store_id.like(f'{store_id}')). \
        filter(SparePartStore.spare_part_id.like(f'{spare_part_id}')).first()


def update_stock(old_stock, quantity):
    try:
        old_stock.stock -= quantity
        session.commit()
    except:
        session.rollback()


def find_different_store(spare_part_id, store_id, quantity):
    return session.query(SparePartStore).filter(SparePartStore.spare_part_id.like(f'{spare_part_id}')). \
        filter(SparePartStore.store_id.notlike(f'{store_id}')).\
        filter(SparePartStore.stock >= quantity).all()
