use carparts;

INSERT INTO suppliers
(supplier_name,
supplier_phone_nr,
supplier_email,
supplier_address,
supplier_contact_first_name,
supplier_contact_last_name)
VALUES
('Autocars' , '031-123456', 'autocars@mail.com', 'Storgatan 25, goteborg', 'Jake', 'Bossman'),
('Autotune', '031-654321', 'auto@tune.com', 'industrivägen 12, goteborg', NULL, NULL);


INSERT INTO manufacturers (manufacturer_name, manufacturer_phone_nr, manufacturer_address)
VALUES
('Oskar', '32423423', 'Göteborg'),
('Astrid', '32238799', 'Göteborg'),
('Andreas', '42389423', 'Göteborg'),
('Oscar', 'jklkjkl42389423', 'Göteborg');


INSERT INTO car_models
(model_name,
brand_name)
VALUES
('Bugatti','Bugatti Veyron'),
('Ferrari','Ferarri 125-S'),
('Lamborghini','Lamborghini Aventador');


INSERT INTO stores
(store_name,
store_phone_nr,
store_email,
store_address)
VALUES
('Gothenburg', '1258125','Gbg@mejl.com', 'Goteborgsvagen 23'),
('Linkoping','1254856','Lin@mejel.com', 'Linvagen 23'),
('Malmo', '125487', 'Malmo@mejl.com','Malmovagen 23'),
('Stockholm','12544646','Stockholm@mejl.com', 'Stockholmsvagen 23');

INSERT INTO employees
(employee_name,
employee_lastname,
employee_phone_nr,
employee_email,
store_id)
VALUES
('Anakin','Skywalker','123123','Anakin@mejl.com', 1),
('Mando','Mandalorian','321321','Mando@mejl.com', 2),
('Yoda','Master','258258','Yoda@mejl.com', 3),
('Luke','Skywalker','951254','Luke@mejl.com', 4),
('Fredrik','Reinfeldt','653258','Fredrik@mejl.com', 2),
('Carl-Gustav','Bernadotte','0202020','Carl@mejl.com', 1);


INSERT INTO customers
(customer_type)
VALUES
(2),
(1);

INSERT INTO spare_parts
(product_nr,
manufacturer_id,
supplier_id,
Description,
purchase_price,
selling_price,
reorder_level,
order_quantity,
estimated_time_of_arrival)
VALUES
('123', 1, 1, 'Headlight', 19.99, 25.99, 3, 10, '2020-11-11'),
('23', 1, 1, 'horn',8.55, 10.90, 10, 20, '2020-12-01'),
('6858', 1, 1, 'tire', 55.90, 69.90, 20, 20, '2020-11-30'),
('4234v2', 1, 1, 'Air filter', 5.99, 10.00, 10, 30, '2021-01-01');


INSERT INTO company_customers
(customer_id,
company_customer_company_name,
company_customer_first_name,
company_customer_last_name,
company_customer_phone,
company_customer_email)
VALUES
(2, 'Apple', 'Steve', 'Jobs', '123465789', 'apple@apple.com');


INSERT INTO private_customers
(customer_id,
private_customer_first_name,
private_customer_last_name,
private_customer_phone,
private_customer_email)
VALUES
(1, 'Joakim', 'Wassberg', '98564321', 'jokkeboii@python.com');


INSERT INTO customer_cars
(customer_registration_nr,
customer_id,
customer_car_brand,
customer_car_model,
customer_car_model_year,
customer_car_color)
VALUES
('ABC 123', 1, 'SAAB', '9-3', 2004, 'Silver-ish'),
('AAA 999', 2, 'VÖLVO', 'XC-800', 2035, 'grön');


INSERT INTO company_contacts
(manufacturer_contact_name,
manufacturer_contact_phone_nr,
manufacturer_contact_email,
manufacturer_contact_id)
VALUES
('Arvid', '0707-070707', 'Company@mail.com', 1),
('David', '0707-707070', 'Company2@mail.com', 2);


INSERT INTO orders
(customer_id,
employee_id,
store_id,
order_date
)
VALUES
(1, 1, 1, '2020-11-17'),
(1, 2, 2, '2020-11-17'),
(2, 3, 3, '2020-11-17'),
(2, 5, 4, '2020-11-17');

INSERT INTO order_details
(spare_part_id,
order_id,
Quantity)
VALUES
(1, 2, 5),
(2, 3, 5),
(3, 4, 6);

INSERT INTO spare_part_stores
(spare_part_id,
store_id,
stock_location,
stock)
VALUES
(1, 1, 'A1', 45),
(1, 2, 'A2', 30),
(1, 3, 'A3', 15),
(1, 4, 'A1', 10),
(2, 1, 'B3', 6),
(2, 2, 'C1', 19),
(2, 3, 'A2', 7),
(2, 4, 'A5', 8),
(3, 1, 'A1', 30),
(3, 2, 'A4', 27),
(3, 3, 'C4', 19),
(3, 4, 'D5', 11),
(4, 1, 'A4', 7),
(4, 2, 'B1', 15),
(4, 3, 'F1', 19),
(4, 4, 'A3', 22);

INSERT INTO car_models_spare_parts
(car_model_id,
spare_part_id)
VALUES
(1, 1),
(2, 2),
(3, 3);
