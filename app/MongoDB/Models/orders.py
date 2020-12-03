from MongoDB.db import Document, db
from MongoDB.Models.stores import Store
import MongoDB.Models.employees as me
from MongoDB.Models.customers import Customer
import MongoDB.Models.spare_parts as ms


class Order(Document):
    collection = db.orders

    def __init__(self, data):
        super().__init__(data)
        for order in self.order_detail:
            order.update({"spare_part": ms.SparePart.find(_id=order["spare_part_id"]).first_or_none()})

    @property
    def store(self):
        return Store.find(_id=self.store_id).first_or_none()

    @property
    def employee(self):
        return me.Employee.find(_id=self.employee_id).first_or_none()

    @property
    def customer(self):
        return Customer.find(_id=self.customer_id).first_or_none()
