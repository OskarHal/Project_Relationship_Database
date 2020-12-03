from MongoDB.db import Document, db
from MongoDB.Models.stores import Store


class Employee(Document):
    collection = db.employees

    @property
    def store(self):
        return Store.find(_id=self.store_id).first_or_none()

