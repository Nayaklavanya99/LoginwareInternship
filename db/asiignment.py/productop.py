import sqlite3 as sl

conn = sl.connect("Product.db")
cur = conn.cursor()





# try:
#     cur.execute("""INSERT INTO PRODUCT VALUES(126,"Pen",-9,90)""")
# except sl.IntegrityError as e:
#     print(f"Integrity Constraint Violated \n {e}")
# except Exception as e:
#     print(f"Exception raised {e}")

try:
    fetch_query = """SELECT COUNT(Product_ID) from PRODUCT"""
    cur.execute(fetch_query)
    data = cur.fetchall()
    print(data[0][0])
except sl.OperationalError as e:
    print(f"Operational Error \n {e}")
except Exception as e:
    print(f"Exception raised {e}")

conn.commit()
conn.close()
