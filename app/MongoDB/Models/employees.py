from MongoDB.db import Document, db


class Employee(Document):
    collection = db.employees
