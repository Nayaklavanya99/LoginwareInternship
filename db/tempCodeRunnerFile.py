cur.execute("""CREATE TABLE Student (First_name TEXT NOT NULL,
            Last_name TEXT NOT NULL,
            Age INTEGER NOT NULL,
            Email TEXT NOT NULL UNIQUE)""")
