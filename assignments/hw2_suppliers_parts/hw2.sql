-- AIN3003 HW2: Suppliers, Parts, Catalog ve Orders tabloları

-- Database oluştur
CREATE DATABASE IF NOT EXISTS suppliers_parts;
USE suppliers_parts;


-- Task 1: Tabloları oluştur (DDL)

DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Catalog;
DROP TABLE IF EXISTS Parts;
DROP TABLE IF EXISTS Suppliers;

CREATE TABLE Suppliers (
    sid    INT PRIMARY KEY,
    sname  VARCHAR(50) NOT NULL,
    city   VARCHAR(50),
    street VARCHAR(100)
) ENGINE=InnoDB;

CREATE TABLE Parts (
    sku         INT PRIMARY KEY,
    pname       VARCHAR(50) NOT NULL,
    stock_level INT,
    color       VARCHAR(20)
) ENGINE=InnoDB;

CREATE TABLE Catalog (
    sid        INT,
    sku        INT,
    unit_price FLOAT NOT NULL,
    PRIMARY KEY (sid, sku),
    FOREIGN KEY (sid) REFERENCES Suppliers(sid),
    FOREIGN KEY (sku) REFERENCES Parts(sku)
) ENGINE=InnoDB;

CREATE TABLE Orders (
    oid      INT PRIMARY KEY,
    sid      INT NOT NULL,
    sku      INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (sid) REFERENCES Suppliers(sid),
    FOREIGN KEY (sku) REFERENCES Parts(sku)
) ENGINE=InnoDB;

-- Task 2: Örnek veri ekle (DML)

INSERT INTO Suppliers (sid, sname, city, street) VALUES
    (1, 'Kayacan A.Ş.', 'Istanbul', 'Istiklal Cad. 10'),
    (2, 'Berat Mert Metal', 'Istanbul', 'Barbaros Blv. 25'),
    (3, 'BAU Tools', 'Ankara', 'Ataturk Blv. 5'),
    (4, 'AIN Parts', 'Izmir', 'Kordon Cad. 42');

INSERT INTO Parts (sku, pname, stock_level, color) VALUES
    (101, 'Bolt', 500, 'red'),
    (102, 'Nut', 800, 'blue'),
    (103, 'Washer', 300, 'red'),
    (104, 'Gear', 50, 'green'),
    (105, 'Spring', 120, 'black');

INSERT INTO Catalog (sid, sku, unit_price) VALUES
    (1, 101,  0.50),
    (1, 103,  0.15),
    (1, 104, 12.00),
    (2, 102,  0.25),
    (2, 103,  0.25),
    (2, 105,  1.50),
    (3, 104, 11.00),
    (3, 105,  1.20),
    (4, 101,  0.55),
    (4, 104, 13.50);

INSERT INTO Orders (oid, sid, sku, quantity) VALUES
    (1, 1, 101, 100),
    (2, 1, 104,   5),
    (3, 2, 102, 200),
    (4, 2, 105,  20),
    (5, 2, 103,  80),
    (6, 3, 104,  10),
    (7, 4, 101,  40);

COMMIT;

-- Task 3: Kırmızı parça sağlayan tedarikçilerin adları

SELECT DISTINCT s.sname
FROM Suppliers s
JOIN Catalog c ON s.sid = c.sid
JOIN Parts p ON c.sku = p.sku
WHERE p.color = 'red';

-- Task 4: Toplam sipariş değeri en az 100.0 olan tedarikçiler

SELECT s.sid, s.sname, ROUND(SUM(o.quantity * c.unit_price), 2) AS total_value
FROM Suppliers s
JOIN Orders o ON s.sid = o.sid
JOIN Catalog c ON o.sid = c.sid AND o.sku = c.sku
GROUP BY s.sid, s.sname
HAVING SUM(o.quantity * c.unit_price) >= 100.0
ORDER BY s.sid;
