from Controllers.order_controller import create_order, find_order_by_id, find_order_by_date


def order_menu():
    while True:
        print("1. Create order")
        print("2. Find order by id")
        print("3. Find order by date")
        print("0. Exit")
        selection = input("> ")

        if selection == "1":
            create_order()
        elif selection == "2":
            order_id = input("Enter order id: ")
            order = find_order_by_id(order_id)
            print("===================")
            if order.customer.customer_type == 1:
                print("test")
                print(f'Order by customer {order.customer.comp_customer[0].company_customer_first_name} '
                      f'{order.customer.comp_customer[0].company_customer_last_name},'
                      f'employee {order.employees.employee_name} '
                      f'in store {order.store.store_name} made on {order.order_date}')
            elif order.customer.customer_type == 2:
                print(f'Order by customer {order.customer.priv_customer[0].private_customer_first_name} '
                      f'{order.customer.priv_customer[0].private_customer_last_name}, '
                      f'employee {order.employees.employee_name} '
                      f'in store {order.store.store_name} made on {order.order_date}')

        elif selection == "3":
            order_date = input("Enter order date (yyyy-mm-dd): ")
            orders = find_order_by_date(order_date)
            print("===================")
            for order in orders:
                if order.customer.customer_type == 1:
                    print(f'Order by customer{order.customer.comp_customer[0].company_customer_first_name} '
                          f'{order.customer.comp_customer[0].company_customer_last_name},'
                          f'employee {order.employees.employee_name} '
                          f'in store {order.store.store_name} made on {order.order_date}')
                elif order.customer.customer_type == 2:
                    print(f'Order by customer{order.customer.priv_customer[0].private_customer_first_name} '
                          f'{order.customer.priv_customer[0].private_customer_last_name}, '
                          f'employee {order.employees.employee_name} '
                          f'in store {order.store.store_name} made on {order.order_date}')

            print("")
        elif selection == "0":
            break
