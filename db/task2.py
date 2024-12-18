import sqlite3 as sl

conn = sl.connect('task2.db')
cur = conn.cursor()
try:
    create_person_table = """CREATE TABLE IF NOT EXISTS person(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NULL
    )"""
    cur.execute(create_person_table)
    print("Created")
except sl.Error as e:
    print("I am error", e)

data_of_person = [("Sahil",23), ("Sahil",24), ("Sahil",25)]
try:
    insert_into_person = """
    INSERT INTO person (name, age) VALUES (?, ?)
    """
    cur.executemany(insert_into_person, data_of_person)    
except sl.Error as e:
    print(e)    

conn.commit()
conn.close()
