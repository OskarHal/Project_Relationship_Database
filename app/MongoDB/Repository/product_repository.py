from MongoDB.Models.spare_parts import SparePart as MongoSparePart


def get_product_by_product_nr(product_nr: str):
    return MongoSparePart.find(product_nr=product_nr).first_or_none()


def update_product(product: MongoSparePart, attribute_name, new_value):

    product[attribute_name] = new_value
    # product.__dict__[attribute_name] = new_value
    # product.__dict__.update({attribute_name: new_value})
    # product.__setattr__(attribute_name, new_value)

    print(product.order_quantity)
    product.save()


def delete_product(product):
    success = False
    try:
        product.delete(_id=product._id)
        success = True
    except:
        print("Something went wrong...")
    finally:
        return success


def get_product_by_id(product_id: str):
    return MongoSparePart.find(_id=product_id).first_or_none()