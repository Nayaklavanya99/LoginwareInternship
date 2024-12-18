import sqlite3 as sl

conn = sl.connect("Product.db")
cur=conn.cursor()


create_product_table= """CREATE TABLE IF NOT EXISTS PRODUCT (
    Product_Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL UNIQUE,
    Price REAL NOT NULL CHECK(Price > 0),
    Quantity INTEGER NOT NULL DEFAULT 0
    )"""
    
cur.execute(create_product_table)

data_of_Products=[("Water Bottle",100,23),
                  ("Android TV",35000,24),
                  ("Macbook",1400000,3),
                  ("Pen",5,90)]
try:
    insert_into_product = """INSERT INTO PRODUCT(Name,Price,Quantity) VALUES(?,?,?)"""
    cur.executemany(insert_into_product,data_of_Products)
except sl.IntegrityError:
    print("Integrity Constraint Violated")

conn.commit()
conn.close()