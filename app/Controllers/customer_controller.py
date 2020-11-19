import Data.Repository.company_customer_repository as ccr
import Data.Repository.private_customer_repository as pcr


def get_all_customers(customer_type):
    if customer_type == 1:
        return ccr.get_company_customer()
    elif customer_type == 2:
        return pcr.get_private_customer()



def add_new_company_customer():
    ccr.add_new_company_customer()
    #lägga till kunddata här eller i repot