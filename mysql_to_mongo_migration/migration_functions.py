from Data.Models.suppliers import Supplier
from Data.db import session
from MongoDB.Models.suppliers import Supplier as MongoSupplier


def fix_suppliers():
    suppliers = session.query(Supplier).all()
    for supplier in suppliers:
        as_dict = supplier.__dict__
        del as_dict["_sa_instance_state"]

        mongo_supplier = MongoSupplier(as_dict)
        mongo_supplier.save()


# def fix_products():
#     products = session.query(Product).all()
#     for product in products:
#         as_dict = product.__dict__
#         as_dict['buyPrice'] = float(as_dict['buyPrice'])
#         as_dict['MSRP'] = float(as_dict['MSRP'])
#         as_dict['productline'] = product.productline.__dict__
#         del as_dict['_sa_instance_state']
#         del as_dict['productline']['_sa_instance_state']
#
#         as_dict['productline'] = {key: value for key, value in as_dict['productline'].items() if value is not None}
#
#         mongo_product =mm.Product(as_dict)
#         mongo_product.save()