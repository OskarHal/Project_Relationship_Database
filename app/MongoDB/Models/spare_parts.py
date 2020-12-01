from MongoDB.db import Document, db


class SparePart(Document):
    collection = db.spare_parts
