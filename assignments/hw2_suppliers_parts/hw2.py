from mysql import connector

# MySQL'e bağlan
my_connection = connector.connect(
    host="localhost", user="root", password="YOUR_PASSWORD"
)

my_cursor = my_connection.cursor()

# Database'i yoksa oluştur varsa bağlan
my_cursor.execute("CREATE DATABASE IF NOT EXISTS suppliers_parts")
my_cursor.execute("USE suppliers_parts")

print("Bağlantı tamam, suppliers_parts seçildi.\n")


# Task 1: Tabloları oluştur (DDL)

# Dosya tekrar çalıştırılınca hata vermesin diye önce eski tabloları sil
# Silme sırası oluşturmanın tersi: önce child sonra parent tablolar

my_cursor.execute("DROP TABLE IF EXISTS Orders, Catalog, Parts, Suppliers")

# Parent tablo: tedarikçiler
my_cursor.execute("""
CREATE TABLE Suppliers (
    sid    INT PRIMARY KEY,
    sname  VARCHAR(50) NOT NULL,
    city   VARCHAR(50),
    street VARCHAR(100)
) ENGINE=InnoDB
""")

# Parent tablo: parçalar
my_cursor.execute("""
CREATE TABLE Parts (
    sku         INT PRIMARY KEY,
    pname       VARCHAR(50) NOT NULL,
    stock_level INT,
    color       VARCHAR(20)
) ENGINE=InnoDB
""")

# Child tablo: hangi tedarikçi hangi parçayı ne kadara satıyor
# PK iki kolondan oluşuyor: (sid, sku)
my_cursor.execute("""
CREATE TABLE Catalog (
    sid        INT,
    sku        INT,
    unit_price FLOAT NOT NULL,
    PRIMARY KEY (sid, sku),
    FOREIGN KEY (sid) REFERENCES Suppliers(sid),
    FOREIGN KEY (sku) REFERENCES Parts(sku)
) ENGINE=InnoDB
""")

# Child tablo: siparişler
my_cursor.execute("""
CREATE TABLE Orders (
    oid      INT PRIMARY KEY,
    sid      INT NOT NULL,
    sku      INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (sid) REFERENCES Suppliers(sid),
    FOREIGN KEY (sku) REFERENCES Parts(sku)
) ENGINE=InnoDB
""")

# Kontrol: Tablolar oluştu mu?
print("Task 1: Tables")
my_cursor.execute("SHOW TABLES")
for row in my_cursor:
    print(row[0])
print()


# Task 2: Örnek veri ekle (DML)

my_cursor.execute("""
INSERT INTO Suppliers (sid, sname, city, street) VALUES
    (1, 'Kayacan A.Ş.', 'Istanbul', 'Istiklal Cad. 10'),
    (2, 'Berat Mert Metal', 'Istanbul', 'Barbaros Blv. 25'),
    (3, 'BAU Tools', 'Ankara', 'Ataturk Blv. 5'),
    (4, 'AIN Parts', 'Izmir', 'Kordon Cad. 42')
""")

my_cursor.execute("""
INSERT INTO Parts (sku, pname, stock_level, color) VALUES
    (101, 'Bolt',   500, 'red'),
    (102, 'Nut',    800, 'blue'),
    (103, 'Washer', 300, 'red'),
    (104, 'Gear',    50, 'green'),
    (105, 'Spring', 120, 'black')
""")

my_cursor.execute("""
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
    (4, 104, 13.50)
""")

my_cursor.execute("""
INSERT INTO Orders (oid, sid, sku, quantity) VALUES
    (1, 1, 101, 100),
    (2, 1, 104,   5),
    (3, 2, 102, 200),
    (4, 2, 105,  20),
    (5, 2, 103,  80),
    (6, 3, 104,  10),
    (7, 4, 101,  40)
""")

# INSERT'leri kalıcı yap
my_connection.commit()

print("-Task 2: Table'lara örnek veriler eklendi-")


# Task 3: Kırmızı parça sağlayan tedarikçi isimleri

my_cursor.execute("""
SELECT DISTINCT s.sname
FROM Suppliers s
JOIN Catalog c ON s.sid = c.sid
JOIN Parts p ON c.sku = p.sku
WHERE p.color = 'red'
""")

print("{:20}".format("\nKırmızı parça tedarikçileri:"))
for row in my_cursor:
    print(f"{row[0]:20}")

# Task 4: Toplam sipariş değeri en az 100.0 olan tedarikçiler


my_cursor.execute("""
SELECT s.sid, s.sname, ROUND(SUM(o.quantity * c.unit_price), 2) AS total_value
FROM Suppliers s
JOIN Orders o ON s.sid = o.sid
JOIN Catalog c ON o.sid = c.sid AND o.sku = c.sku
GROUP BY s.sid, s.sname
HAVING SUM(o.quantity * c.unit_price) >= 100.0
ORDER BY s.sid
""")

print(
    "{:5} {:20} {:15}".format(
        "\nToplam siparişi min 100 olan tedarikçiler: \nsid",
        "Supplier Name",
        "Total Value",
    )
)
for row in my_cursor:
    print(f"{row[0]:<5} {row[1]:20} {row[2]:<15.2f}")

my_cursor.close()
my_connection.close()
