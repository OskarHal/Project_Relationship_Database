from MongoDB.db import Document, db


class Orders(Document):
    collection = db.orders
