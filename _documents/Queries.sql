use carparts2;

INSERT INTO spareparts (ProductNr, ManufacturerId, SupplierId, Description, PurchasePrice, SellingPrice, ReorderLevel, OrderQuantity, EstimatedTimeOfArrival) 
VALUES 
('43243', 2, 1, "Spik", 34.43, 40.00, 23, 4, '2020-12-24');

/* Se vilka spareparts som varje manufacturer tillverkar*/

SELECT man.Name, s.Description as 'Sparepart name' FROM spareparts s
JOIN manufacturers man on man.ManufacturerId=s.ManufacturerId;

/* Få ut kontaktuppgift från tillverkare för reservdel med specifikt produktnummer */

SELECT m.Name as 'manufacturer name', s.ProductNr, s.Description as 'product name', c.Name as 'company contact', c.Email, c.PhoneNr from company_contacts c
JOIN manufacturers m on m.ManufacturerId=c.ManufacturerId
JOIN spareparts s on s.ManufacturerId=m.ManufacturerId
WHERE s.ProductNr='123';

/* Få ut alla orderar från privata kunder */

SELECT CONCAT(priv.FirstName + ' ', priv.LastName) AS FullName, o.OrderDate FROM private_customers priv
JOIN customers c on priv.CustomerId=c.CustomerId
JOIN orders o on c.CustomerId=o.CustomerId;

/* Summan av värdet för alla ordrar på privata kunder samt företagskunder */

SELECT SUM(o.Quantity) AS TotalItemsOrdered, SUM(o.Quantity * s.SellingPrice) as 'TotalValue'  FROM order_details o
JOIN spareparts s on o.SparepartId= s.SparepartId;


/* Hämta alla affärer som har en specifik sparepart */

SELECT st.Name as 'Store', s.ProductNr, spst.Quantity FROM stores st
JOIN spareparts_stores spst on st.StoreId=spst.stores_StoreId
JOIN spareparts s on spst.spareparts_SparepartId=s.SparepartId
WHERE ProductNr=123;

SELECT * FROM spareparts_stores spst
JOIN stores st on spst.stores_StoreId=st.StoreId
JOIN spareparts s on spst.spareparts_SparepartId=s.SparepartId
WHERE ProductNr=123;

/* Hämta alla modeller som en specifik sparepart passar till samt ta med tillverkaren */

INSERT INTO carmodels_spareparts(carmodel_id, sparepart_id)
VALUES
(2, 1);

SELECT ca.model_name as 'modelName', sp.Description as 'SparepartName', ma.Name 'Manufacturer' FROM carmodels_spareparts casp
JOIN carmodels ca on casp.carmodel_id=ca.carmodel_id
JOIN spareparts sp on casp.sparepart_id=sp.SparepartId
JOIN manufacturers ma on sp.ManufacturerId=ma.ManufacturerId
WHERE sp.ProductNr=123;

/* Vilka bilar har privatkunder samt företagskunder */

SELECT ca.Brand, ca.Model,
CASE 
	WHEN cu.CustomerType = 1 
		THEN 'private' 
	ELSE 'company' 
END AS CustomerType 
FROM customers cu
LEFT JOIN private_customers pricu on cu.CustomerId=pricu.CustomerId
LEFT JOIN company_customers cocu on cu.customerId=cocu.CustomerId
JOIN customer_cars ca on cu.CustomerId=ca.CustomerId;

/* Hämta företagskontakt till tillverkare nr 3 */

SELECT coca.Name as 'Contact', coca.Email, coca.PhoneNr FROM company_contacts coca
JOIN manufacturers ma on coca.ManufacturerId=ma.ManufacturerId
WHERE ma.ManufacturerId=2;

/* Lägg till en ny order */

INSERT INTO orders (CustomerId, EmployeeId, StoreId, OrderDate)
VALUES
(1, 2, 1, '2020-12-24');

SELECT * FROM orders o
ORDER BY o.OrderDate DESC;

INSERT INTO order_details(SparepartId, OrderId,Quantity)
VALUES
(1, 5, 3);

/* Ta bort en kund */

DELETE FROM customers 
WHERE customerid=1;

/*Ta ut alla förnamn för employees*/

SELECT em.FirstName FROM employees em;

/*Ta ut alla butiker samt vilka reservdelar de har*/

SELECT st.Name as 'Store', sp.Description as 'SparepartName', spst.Quantity FROM spareparts_stores spst
JOIN spareparts sp on spst.spareparts_SparepartId=sp.SparepartId
JOIN stores st on spst.stores_StoreId=st.StoreId
WHERE spst.Quantity > 0;

/*Hämta alla bilmodeller som det finns reservdelar till samt i vilka butiker som de finns i och hur många som finns*/

 SELECT ca.brand_name, ca.model_name, sp.ProductNr, sp.Description as 'SparePartName', st.Name, spst.Quantity FROM carmodels_spareparts casp
 JOIN carmodels ca on casp.carmodel_id=ca.carmodel_id
 JOIN spareparts sp on casp.sparepart_id=sp.SparepartId
 JOIN spareparts_stores spst on sp.SparepartId=spst.spareparts_SparepartId
 JOIN stores st on spst.stores_StoreId=st.StoreId
 WHERE Quantity > 0;

 /*Hämta mejladress till en tillverkare för reservdel med description 'horn'*/
 
SELECT sp.Description 'SparePartName', ma.Name as 'CompanyName', coco.Name as 'contact', coco.Email, coco.PhoneNr FROM spareparts sp
JOIN manufacturers ma on sp.ManufacturerId=ma.ManufacturerId
JOIN company_contacts coco on ma.ManufacturerId=coco.ManufacturerId
WHERE sp.Description='horn';

/* Vilken tillverkare av reservdel hade kund nummer 2*/

SELECT cu.CustomerId, cuca.Brand, cuca.Model, sp.Description as 'SparePartName', ma.Name 'ManufacturerName' FROM customers cu
JOIN customer_cars cuca on cu.CustomerId=cuca.CustomerId
JOIN orders o on cu.CustomerId=o.CustomerId
JOIN order_details orde on o.OrderId=orde.OrderDetailId
JOIN spareparts sp on orde.SparepartId=sp.SparepartId
JOIN manufacturers ma on sp.ManufacturerId=ma.ManufacturerId
WHERE cu.CustomerId=2;

/* Testar att skapa view table */

CREATE VIEW a AS SELECT sp.ProductNr, sp.Description AS 'Name', s.Name AS City, s.Adress, ss.StockLocation AS 'Stock location', ss.Quantity FROM spareparts sp
JOIN spareparts_stores ss ON sp.SparepartId = ss.spareparts_SparepartId
JOIN stores s ON ss.stores_StoreId = s.StoreId;

SELECT * from a;

UPDATE stores SET Name = 'Norrköping'
WHERE StoreId = 2;

/* Se vilka ordrar och kunder som vissa anställda har haft */

select e.FirstName, o.OrderDate, priv.FirstName, comp.Name From employees e
join orders o USING(EmployeeId)
join customers c USING(CustomerId)
left join private_customers priv USING(CustomerId)
left join company_customers comp USING(CustomerId);
