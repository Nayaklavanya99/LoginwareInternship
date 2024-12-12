import sqlite3 as sl

conn = sl.connect("Library.db")

cur  = conn.cursor()

# fetch_query = """SELECT DISTINCT(Author) FROM Book WHERE Author = "Fyodor Dostoesky" AND Price>100"""
# fetch_query = """SELECT Author FROM Book WHERE Author = "Fyodor Dostoesky" OR Price>100"""
# fetch_query = """SELECT * FROM Book ORDER BY Price ASC"""
# fetch_query = """SELECT Title FROM Book ORDER BY Price DESC limit 1"""
# fetch_query = """SELECT Title FROM Book WHERE Book_id BETWEEN 1 AND 3 ORDER BY Title ASC LIMIT 2"""
# fetch_query = """UPDATE Book SET PUBLISHER='ABC' WHERE Price>1"""
# fetch_query = """DELETE from Book where Book_id=3"""

cur.execute(fetch_query)
Books = cur.fetchall()

# var = ('abc',360)
# cur.execute("UPDATE Book SET PUBLISHER=? WHERE Price=?", var)

for i in Books:
#     print(f"ID: {i[0]}")
#     print(f"Title: {i[1]}")
#     print(f"Author: {i[2]}")
#     print(f"ISBN : {i[3]}")
#     print(f"YEAR: {i[4]}")
#     print(f"Price: {i[5]}")
    print(f"Publisher: {i[6]}")
#     print("-"*20)
#     # print(i)

# for i in Books:
#     print(i)
# print(Books)
conn.commit()
conn.close()
print("Done")
