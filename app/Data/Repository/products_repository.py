from Data.Models.car_models import CarModel
from Data.Models.manufacturers import Manufacturer
from Data.Models.spare_part_stores import SparePartStore
from Data.Models.spare_parts import SparePart
from Data.Models.suppliers import Supplier
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


def add_product(product: SparePart):
    success = False
    try:
        session.add(product)
        session.commit()
        success = True
    except:
        session.rollback()
    finally:
        return success
    """
    spare_part_store = SparePartStore(stock=4, stock_location="A3", store_id=1)
    car_model = session.query(CarModel).filter(CarModel.car_model_id == 1).first()
    new_car_model = CarModel(model_name="v90", brand_name="Tesla")
    manufacturer = session.query(Manufacturer).filter(Manufacturer.manufacturer_id == 1).first()
    supplier = session.query(Supplier).filter(Supplier.supplier_id == 1).first()
    product.manufacturer = manufacturer
    product.supplier = supplier
    product.stores.append(spare_part_store)
    product.car_models.append(new_car_model)
    session.add(product)
    session.commit()
    product.print_all_information_with_relationships()
    """


def get_all_stores():
    return session.query(SparePartStore).all()


def get_car_model_by_id(car_model_id):
    return session.query(CarModel).filter(CarModel.car_model_id == car_model_id).first()


def get_manufacturer_by_id(manufacturer_id):
    return session.query(Manufacturer).filter(Manufacturer.manufacturer_id == manufacturer_id).first()


def get_supplier_by_id(supplier_id):
    return session.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()


def get_all_car_models():
    return session.query(CarModel).all()
