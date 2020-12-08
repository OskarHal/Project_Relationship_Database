from MongoDB.db import Document, db
import MongoDB.Models.employees as me


class Store(Document):
    collection = db.stores

    @property
    def employees(self):
        return me.Employee.find(store_id=self._id)
