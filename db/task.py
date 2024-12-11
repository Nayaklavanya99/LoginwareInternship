import sqlite3 as sl

conn = sl.connect("College.db")

cur = conn.cursor()

# creating Student Table
# cur.execute("DROP TABLE IF EXISTS Student")
create_student_query = """CREATE TABLE IF NOT EXISTS Student(First_name TEXT NOT NULL DEFAULT 'Not Provided',
            Last_name TEXT NOT NULL DEFAULT 'Not Provided',
            Age INTEGER NOT NULL DEFAULT 0,
            Email TEXT NOT NULL UNIQUE DEFAULT 'Not Provided')"""
cur.execute(create_student_query)

data = [
    ('Samar','SAMR',23,'samar@gmail.com'),
    ('John','Doe',19,'john.doe@gmail.com'),
    ('Jane','Smith',20,'jane.smith@gmail.com'),
    ('Mike','Johnson',22,'mike.j@gmail.com'),
    ('Sarah','Williams',21,'sarah.w@gmail.com'),
    ('David','Brown',20,'david.b@gmail.com'),
    ('Emily','Davis',19,'emily.d@gmail.com'),
    ('James','Miller',23,'james.m@gmail.com'),
    ('Emma','Wilson',22,'emma.w@gmail.com'),
    ('Alex','Taylor',21,'alex.t@gmail.com'),
]

insert_query = (
    """INSERT INTO Student (First_name,Last_name,Age,Email) VALUES (?, ?, ?, ?)"""
)
cur.executemany(insert_query, data)

conn.commit()
print("Database 2.0")
conn.close()
