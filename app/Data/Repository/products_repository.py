from Data.Models.spare_parts import SparePart
from Data.db import session


def get_all_products():
    return session.query(SparePart).all()


def get_product_by_product_nr(product_nr: str):
    return session.query(SparePart).filter(SparePart.product_nr == product_nr).first()


def get_products_by_product_description_pattern(description_pattern: str):
    return session.query(SparePart).filter(SparePart.description.like(f'%{description_pattern}%')).all()


def delete_product(product):
    success = False
    try:
        session.delete(product)
        session.commit()
        success = True
    except:
        session.rollback()
    finally:
        return success


def update_product(product: SparePart, attribute_name, new_value):
    success = False
    try:
        for product_attribute, value in vars(product).items():
            if product_attribute == attribute_name:
                product.__setattr__(product_attribute, new_value)
        session.commit()
        success = True
    except:
        session.rollback()
    finally:
        return success
