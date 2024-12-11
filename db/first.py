import sqlite3 as sl
import email

conn = sl.connect('College.db')

cur = conn.cursor()

# creating Student Table
# cur.execute("DROP TABLE IF EXISTS Student")
create_student_query = """CREATE TABLE IF NOT EXISTS Student(First_name TEXT NOT NULL DEFAULT 'Not Provided',
            Last_name TEXT NOT NULL DEFAULT 'Not Provided',
            Age INTEGER NOT NULL DEFAULT 0,
            Email TEXT NOT NULL UNIQUE DEFAULT 'Not Provided')"""
cur.execute(create_student_query)

# Inserting into Studnet Table
# insert_student_query = """INSERT INTO Student VALUES ('Sahil', 'Belurkar', 22, 'sahilbelurkar14@gmail.com'),
# ('Lavanya', 'Nayak', 23, 'lavanyanayak99@gmail.com')"""
# cur.execute(insert_student_query)

def user_input():
    global name,last_name,age,email
    name = input("Enter your first name: ")
    last_name = input("Enter your last name: ") 
    age = int(input("Enter your age: "))    
    email = input("Enter your email: ")

user_input()
# insert_query= f"""INSERT INTO Student VALUES ('{name}', '{last_name}', {age}, '{email}')"""
insert_query= """INSERT INTO Student (First_name,Last_name,Age,Email) VALUES (?, ?, ?, ?)"""
choice = input("Do you want to add  student? (y/n): ")
if choice == 'y':
    cur.execute(insert_query, (name, last_name, age, email))
else:
    print("No student added")

select_student_query = """SELECT * FROM Student"""
cur.execute(select_student_query)
studentlist = cur.fetchall()

desce = """PRAGMA table_info(Student)"""
cur.execute(desce)
describelist = cur.fetchall()

# Print student records with column descriptions
for i in range(len(studentlist)):
    print(f"{describelist[i][1]}:{studentlist[i][i]}")
conn.commit()
print("Database")
conn.close()
