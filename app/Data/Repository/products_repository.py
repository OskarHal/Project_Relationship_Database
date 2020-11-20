from Data.Models.spare_parts import SparePart
from Data.db import session


def get_all_products():
    return session.query(SparePart).all()