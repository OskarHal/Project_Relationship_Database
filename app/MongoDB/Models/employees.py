import MongoDB.Models.orders as mo
from MongoDB.db import Document, db
import MongoDB.Models.stores as ms


class Employee(Document):
    collection = db.employees

    @property
    def store(self):
        return ms.Store.find(_id=self.store_id).first_or_none()

    @property
    def orders(self):
        return mo.Order.find(employee_id=self._id)

