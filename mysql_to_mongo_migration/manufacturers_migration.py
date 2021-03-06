from Data.Models.company_contacts import ManufacturerContact
from Data.Models.manufacturers import Manufacturer
from Data.db import session
from MongoDB.Models.manufacturers import Manufacturer as MongoManufacturer


def fix_manufacturers():
    manufacturers = session.query(Manufacturer).all()

    for manufacturer in manufacturers:
        as_dict = manufacturer.__dict__

        if manufacturer.company_contacts is not None:
            contact_list_dict = []
            for contact in manufacturer.company_contacts:
                contact_list_dict.append({'manufacturer_contact_name': contact.manufacturer_contact_name,
                                          'manufacturer_contact_phone_nr': contact.manufacturer_contact_phone_nr,
                                          'manufacturer_contact_email': contact.manufacturer_contact_email})
            as_dict.update({'company_contacts': contact_list_dict})

        del as_dict['_sa_instance_state']

        mongo_manufacturer = MongoManufacturer(as_dict)
        mongo_manufacturer.save()
