from MongoDB.db import Document, db


class Customers(Document):
    collection = db.customers
