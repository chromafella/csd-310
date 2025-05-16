DROP DATABASE IF EXISTS Bacchus_Winery;
CREATE DATABASE Bacchus_Winery;
USE Bacchus_Winery;


CREATE TABLE Department (
    Department_ID INT PRIMARY KEY AUTO_INCREMENT,
    Department_Name VARCHAR(50) NOT NULL
);


CREATE TABLE Employee (
    Employee_ID INT PRIMARY KEY AUTO_INCREMENT,
    Employee_Name VARCHAR(100) NOT NULL,
    Job_Title VARCHAR(50) NOT NULL,
    Department_ID INT,
    Total_Hours INT DEFAULT 0,
    FOREIGN KEY (Department_ID) REFERENCES Department(Department_ID)
);


ALTER TABLE Department 
ADD COLUMN Manager_ID INT,
ADD CONSTRAINT FK_Manager 
FOREIGN KEY (Manager_ID) REFERENCES Employee(Employee_ID);


CREATE TABLE Work_Hours (
    Work_Hours_ID INT PRIMARY KEY AUTO_INCREMENT,
    Employee_ID INT,
    Hours_Worked INT,
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID)
);


CREATE TABLE Supplier (
    Supplier_ID INT PRIMARY KEY AUTO_INCREMENT,
    Supplier_Name VARCHAR(100) NOT NULL,
    Contact_Info VARCHAR(150) NOT NULL
);


CREATE TABLE Supply (
    Supply_ID INT PRIMARY KEY AUTO_INCREMENT,
    Supply_Type VARCHAR(50) NOT NULL,
    Quantity INT,
    Supplier_ID INT,
    Order_Date DATE,
    Expected_Delivery DATE,
    Actual_Delivery DATE,
    FOREIGN KEY (Supplier_ID) REFERENCES Supplier(Supplier_ID)
);


CREATE TABLE Wine (
    Wine_ID INT PRIMARY KEY AUTO_INCREMENT,
    Wine_Name VARCHAR(50) NOT NULL,
    Total_Produced INT DEFAULT 0,
    Total_Distributed INT DEFAULT 0
);


CREATE TABLE Inventory (
    Inventory_ID INT PRIMARY KEY AUTO_INCREMENT,
    Wine_ID INT,
    In_Stock INT DEFAULT 0,
    Last_Updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Wine_ID) REFERENCES Wine(Wine_ID)
);



CREATE TABLE Distributor (
    Distributor_ID INT PRIMARY KEY AUTO_INCREMENT,
    Distributor_Name VARCHAR(100) NOT NULL,
    Dis_Contact_Info VARCHAR(150) NOT NULL
);


CREATE TABLE Wine_Order (
    Order_ID INT PRIMARY KEY AUTO_INCREMENT,
    Distributor_ID INT,
    Wine_ID INT,
    Order_Date DATE,
    Shipping_Date DATE,
    Delivery_Status VARCHAR(50) DEFAULT 'Pending',
    Quantity INT,
    FOREIGN KEY (Distributor_ID) REFERENCES Distributor(Distributor_ID),
    FOREIGN KEY (Wine_ID) REFERENCES Wine(Wine_ID)
);


INSERT INTO Department (Department_Name) VALUES 
('Finance'), ('Marketing'), ('Production'), ('Distribution');

INSERT INTO Employee (Employee_Name, Job_Title, Department_ID, Total_Hours) VALUES 
('Brennan Cheatwood', 'Finance Manager', 1, 200),
('James Guy', 'Marketing Manager', 2, 160),
('Bill Market', 'Marketing Assistant', 2, 140),
('Jack Black', 'Production Manager', 3, 160),
('George Costanza', 'Distribution Manager', 4, 160);


UPDATE Department SET Manager_ID = 1 WHERE Department_ID = 1;
UPDATE Department SET Manager_ID = 2 WHERE Department_ID = 2;
UPDATE Department SET Manager_ID = 4 WHERE Department_ID = 3;
UPDATE Department SET Manager_ID = 5 WHERE Department_ID = 4;

INSERT INTO Work_Hours (Employee_ID, Hours_Worked) VALUES 
(1, 40), (2, 40), (3, 35), (4, 40), (5, 40);

INSERT INTO Supplier (Supplier_Name, Contact_Info) VALUES 
('Bottles and Whatnot Inc.', 'bottlesandwhatnot@yahoo.com'),
('3M Label Department', '3mlabels@2m.com'),
('Corks n Company.', 'corksnco@hotmail.biz');

INSERT INTO Supply (Supply_Type, Quantity, Supplier_ID, Order_Date, Expected_Delivery, Actual_Delivery) VALUES 
('Bottles', 1000, 1, '2025-05-01', '2025-05-05', '2025-05-05'),
('Labels', 2000, 2, '2025-05-02', '2025-05-06', '2025-05-06'),
('Corks', 500, 3, '2025-05-03', '2025-05-07', '2025-05-07');

INSERT INTO Wine (Wine_Name, Total_Produced, Total_Distributed) VALUES 
('Merlot', 500, 300),
('Cabernet', 400, 250),
('Chablis', 300, 200),
('Chardonnay', 600, 400);

INSERT INTO Inventory (Wine_ID, In_Stock) VALUES 
(1, 200), 
(2, 150), 
(3, 100), 
(4, 200);

INSERT INTO Distributor (Distributor_Name, Dis_Contact_Info) VALUES 
('East Coast Distributors', 'contact@eastcoast.com'),
('West Coast Wines', 'contact@westcoast.com'),
('Southside Wine Supply', 'contact@southside.com');

INSERT INTO Wine_Order (Distributor_ID, Wine_ID, Order_Date, Shipping_Date, Delivery_Status, Quantity) VALUES 
(1, 1, '2025-05-05', '2025-05-07', 'Delivered', 50),
(2, 2, '2025-05-06', '2025-05-08', 'Delivered', 30),
(3, 3, '2025-05-07', '2025-05-09', 'Delivered', 20),
(1, 4, '2025-05-08', '2025-05-10', 'Pending', 40);

-- Display Data
SELECT * FROM Department;
SELECT * FROM Employee;
SELECT * FROM Work_Hours;
SELECT * FROM Supplier;
SELECT * FROM Supply;
SELECT * FROM Inventory;
SELECT * FROM Wine;
SELECT * FROM Distributor;
SELECT * FROM Wine_Order;
