from Data.Models.employees import Employee
from Data.Models.stores import Store
from Data.Models.suppliers import Supplier
from Data.db import session
from MongoDB.Models.suppliers import Supplier as MongoSupplier
from MongoDB.Models.stores import Store as MongoStore
from MongoDB.Models.employees import Employee as MongoEmployee


def fix_suppliers():
    suppliers = session.query(Supplier).all()

    for supplier in suppliers:
        as_dict = supplier.__dict__
        del as_dict["_sa_instance_state"]

        mongo_supplier = MongoSupplier(as_dict)




def fix_stores():
    stores = session.query(Store).all()

    for store in stores:
        as_dict = store.__dict__
        del as_dict["_sa_instance_state"]

        mongo_store = MongoStore(as_dict)
        mongo_store.save()


def fix_employees():
    employees = session.query(Employee).all()

    for employee in employees:
        as_dict = employee.__dict__
        as_dict["store_id"] = MongoStore.find(store_id=employee.store_id).first_or_none()._id
        del as_dict["_sa_instance_state"]

        mongo_employee = MongoEmployee(as_dict)
        mongo_employee.save()
