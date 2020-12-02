from MongoDB.db import Document, db


class Order(Document):
    collection = db.orders
