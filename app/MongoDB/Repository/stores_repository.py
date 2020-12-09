from MongoDB.Models.stores import Store


def get_all_stores():
    return Store.all()
