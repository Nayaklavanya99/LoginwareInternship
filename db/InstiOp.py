import sqlite3 as sl

conn = sl.connect("Institute.db")

cur = conn.cursor()

fetch_query = "SELECT * FROM Student"
cur.execute(fetch_query)
data = cur.fetchall()
for row in data:
    print(row)


conn.commit()
conn.close()