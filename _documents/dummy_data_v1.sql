USE carparts;

INSERT INTO `carparts`.`spareparts`
(`ProductNr`,
`ManufacturerId`,
`SupplierId`,
`Description`,
`StockLocation`,
`QuantityInStock`,
`PurchasePrice`,
`SellingPrice`,
`ReorderLevel`,
`OrderQuantity`,
`EstimatedTimeOfArrival`)
VALUES
('123', 1, 1, 'Testdata', 'A1', 20, 19.99, 25.99, 3, 10, '2020-11-11'),
('23', 1, 1, 'horn', 'A2', 30, 8.55, 10.90, 10, 20, '2020-12-01'),
('6858', 1, 1, 'tire', 'A1', 5, 55.90, 69.90, 20, 20, '2020-11-30'),
('4234v2', 1, 1, 'Air filter', 'B0', 13, 5.99, 10.00, 10, 30, '2021-01-01');


INSERT INTO `carparts`.`suppliers`
(`SupplierName`,
`PhoneNr`,
`Email`,
`Adress`,
`ContactFirstName`,
`ContactLastName`)
VALUES
('Autocars' , '031-123456', 'autocars@mail.com', 'Storgatan 25, goteborg', 'Jake', 'Bossman'),
('Autotune', '031-654321', 'auto@tune.com', 'industrivägen 12, goteborg', NULL, NULL);


INSERT INTO `carparts`.`manufacturers` (Name, PhoneNr, Adress)
VALUES
('Oskar', '32423423', 'Göteborg'),
('Astrid', '32238799', 'Göteborg'),
('Andreas', '42389423', 'Göteborg'),
('Oscar', 'jklkjkl42389423', 'Göteborg');


INSERT INTO `carparts`.`carmodels`
(model_name,
brand_name)
VALUES
('Bugatti','Bugatti Veyron'),
('Ferrari','Ferarri 125-S'),
('Lamborghini','Lamborghini Aventador');


INSERT INTO `carparts`.`employees`
(FirstName,
LastName,
PhoneNr,
Email,
StoreId)
VALUES
('Anakin','Skywalker','123123','Anakin@mejl.com', NULL),
('Mando','Mandalorian','321321','Mando@mejl.com', NULL),
('Yoda','Master','258258','Yoda@mejl.com', NULL),
('Luke','Skywalker','951254','Luke@mejl.com', NULL),
('Fredrik','Reinfeldt','653258','Fredrik@mejl.com',NULL),
('Carl-Gustav','Bernadotte','0202020','Carl@mejl.com', NULL);


INSERT INTO `carparts`.`customers`
(CustomerType)
VALUES
(1),
(2);


INSERT INTO `carparts`.`company_customers` 
(CustomerId, Name, ContactFirstName, ContactLastName, PhoneNr, Email)
VALUES
(2, 'Apple', 'Steve', 'Jobs', '123465789', 'apple@apple.com');

INSERT INTO `carparts`.`private_customers`
(CustomerId, FirstName, LastName, PhoneNr, Email )
VALUES
(1, 'Joakim', 'Wassberg', '98564321', 'jokkeboii@python.com');


INSERT INTO `carparts`.`customer_cars`
(RegistrationNr, CustomerId, Brand, Model, ModelYear, Color)
VALUES 
('ABC 123', 1, 'SAAB', '9-3', 2004, 'Silver-ish'),
('AAA 999', 2, 'VÖLVO', 'XC-800', 2035, 'grön');

INSERT INTO `carparts`.`company_contacts`
(`Name`, `PhoneNr`, `Email`, `ManufacturerId`)
VALUES
('Arvid', '0707-070707', 'Company@mail.com', 1),
('David', '0707-707070', 'Company2@mail.com', 2);


INSERT INTO `carparts`.`stores`
(Name, PhoneNr, Email, Adress)
VALUES
('Gothenburg', '1258125','Gbg@mejl.com', 'Goteborgsvagen 23'),
('Linkoping','1254856','Lin@mejel.com', 'Linvagen 23'),
('Malmo', 125487, 'Malmo@mejl.com','Malmovagen 23'),
('Stockholm','12544646','Stockholm@mejl.com', 'Stockholmsvagen 23');

INSERT INTO `carparts`.`orders`
(CustomerId, EmployeeId, StoreId)
VALUES
(1, 1, 1),
(1, 2, 2),
(2, 3, 3),
(2, 5, 4);
