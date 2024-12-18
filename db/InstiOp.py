import sqlite3 as sl

conn = sl.connect("Institute.db")

cur = conn.cursor()

fetch_query = "SELECT * FROM Student"
cur.execute(fetch_query)
data = cur.fetchall()
print(data[0])


conn.commit()
conn.close()