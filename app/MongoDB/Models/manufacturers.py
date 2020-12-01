from MongoDB.db import Document, db


class Manufacturer(Document):
    collection = db.manufacturers
