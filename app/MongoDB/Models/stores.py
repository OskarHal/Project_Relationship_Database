from MongoDB.db import Document, db


class Store(Document):
    collection = db.stores
