from MongoDB.db import Document, db
from MongoDB.Models.stores import Store
import MongoDB.Models.employees as me
from MongoDB.Models.customers import Customer


class Order(Document):
    collection = db.orders

    @property
    def store(self):
        return Store.find(_id=self.store_id).first_or_none()

    @property
    def employee(self):
        return me.Employee.find(_id=self.employee_id).first_or_none()

    @property
    def customer(self):
        return Customer.find(_id=self.customer_id).first_or_none()
