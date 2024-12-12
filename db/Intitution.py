# student table:Student_Id,F_Name,L_Name,Age, Grade,Email,Enrollment_id
#Courses table: Course_id,Course_name,Dept
#Enrollment table: Enrollment_id,Student_id,Course_id,Semester

import sqlite3 as sl

conn = sl.connect('Institute.db')

cur =conn.cursor()

cur.execute("""DROP TABLE IF EXISTS Student""")
cur.execute("""DROP TABLE IF EXISTS Courses""")
cur.execute("""DROP TABLE IF EXISTS Enrollment""")
create_student_query = """CREATE TABLE IF NOT EXISTS Student(
    Student_ID INTEGER PRIMARY KEY,
    F_Name TEXT NOT NULL,
    L_Name TEXT NOT NULL,
    AGE INTEGER NOT NULL,
    Grade TEXT NOT NULL,
    Email TEXT NOT NULL
)"""

create_course_query = """CREATE TABLE IF NOT EXISTS Courses(
    Course_ID INTEGER PRIMARY KEY,
    Course_Name TEXT NOT NULL,
    Dept TEXT NOT NULL
)"""

create_enrollment_query = """CREATE TABLE IF NOT EXISTS Enrollment(
    Enrollment_ID INTEGER PRIMARY KEY,
    Student_ID INTEGER,
    Course_ID INTEGER,
    Semester TEXT NOT NULL,
    FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID),
    FOREIGN KEY (Course_ID) REFERENCES Courses(Course_ID)
)"""

cur.execute(create_student_query)
cur.execute(create_course_query)
cur.execute(create_enrollment_query)

data_of_students = [(123,"Sahil","Belurkar",22,"Second","sahil@gmail.com"),
                   (124,"Lavanya","Nayak",23,"Second","lavanya@gmail.com"),
                   (125,"John","Smith",21,"First","john.s@gmail.com"),
                   (126,"Maria","Garcia",22,"Second","maria.g@gmail.com"),
                   (127,"David","Wilson",20,"First","david.w@gmail.com")]

data_of_courses = [(101, "Mathematics", "Mathematics"),
                   (102, "Physics", "Physics"),
                   (103, "Chemistry", "Chemistry"),
                   (104, "Biology", "Biology"),
                   (105, "Computer Science", "Computer Science")]
data_of_enrollment = [(1, 123, 101, "Second"),
                      (2, 124, 102, "Second"),
                      (3, 125, 103, "First"),
                      (4, 126, 104, "Second"),
                      (5, 127, 105, "First")]

insert_to_student_query = """INSERT INTO Student(Student_ID,F_Name,L_Name,AGE,Grade,Email) VALUES(?,?,?,?,?,?)"""
cur.executemany(insert_to_student_query, data_of_students)

insert_to_course_query = """INSERT INTO Courses(Course_ID,Course_Name,Dept) VALUES(?,?,?)"""
cur.executemany(insert_to_course_query, data_of_courses)

insert_to_enrollment_query = """INSERT INTO Enrollment(Enrollment_ID, Student_ID, Course_ID, Semester) VALUES(?, ?, ?, ?)"""
cur.executemany(insert_to_enrollment_query, data_of_enrollment)

alter_student_query = """ALTER TABLE Student ADD COLUMN Enrollment_ID INTEGER REFERENCES Enrollment(Enrollment_ID)"""
cur.execute(alter_student_query)
update_student_query = """UPDATE Student SET Enrollment_ID = (SELECT Enrollment_ID FROM Enrollment WHERE Student.Student_ID = Enrollment.Student_ID)"""
cur.execute(update_student_query)






conn.commit()
conn.close()
