from Data.Models.spare_parts import SparePart
from Data.db import session


def get_all_products():
    return session.query(SparePart).all()


def get_product_by_product_nr(product_nr: str):
    return session.query(SparePart).filter(SparePart.product_nr == product_nr).first()


def get_product_by_product_description(description_pattern: str):
    return session.query(SparePart).filter(SparePart.description.like(f'%{description_pattern}%')).all()
