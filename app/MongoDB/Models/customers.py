from MongoDB.db import Document, db


class Customer(Document):
    collection = db.customers
