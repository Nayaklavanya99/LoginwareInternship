import sqlite3 as sl
import email

conn = sl.connect("Library.db")

cur = conn.cursor()


cur.execute("DROP TABLE IF EXISTS Book")
create_book_query = """CREATE TABLE IF NOT EXISTS Book(
            Book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL DEFAULT 'Not Provided',
            Author TEXT NOT NULL DEFAULT 'Not Provided', 
            ISBN TEXT UNIQUE,
            Publication_year INTEGER,
            Price REAL DEFAULT 0)"""
cur.execute(create_book_query)
cur.execute('''ALTER TABLE Book ADD COLUMN PUBLISHER TEXT''')
innsert_to_book ="""INSERT INTO Book(Title,Author,ISBN,Publication_year,price ) VALUES("BROTHERS KARMAZOV","Fyodor Dostoesky","ISBN-1980-345",1980,360),
("Metamorphosis","Franz Kafka","ISBN-1989-356",1990,200),
("Letters From Underground","Fyodor Dostoesky","ISBN-1980-385",1985,380)"""
cur.execute(innsert_to_book)


conn.commit()
conn.close()
print("Book table created successfully")