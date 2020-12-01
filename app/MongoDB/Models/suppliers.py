from MongoDB.db import Document, db


class Supplier(Document):
    collection = db.suppliers