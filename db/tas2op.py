import sqlite3 as sl

conn = sl.connect("task2.db")
cur = conn.cursor()


# cur.execute("""INSERT INTO person(name) values("Samar")""")

try:
    # fetch_query = """select Name,count(age) as total_age from person group by name order by total_age ASC"""
    # fetch_query = """select Name,max(age) as age from person where age = age"""
    # fetch_query = """select Name,min(age) as age from person where age = age"""
    fetch_query = """select Name,avg
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    (age) as age from person where age = age"""
    # fetch_query = """select Name,sum(age) as total_age from person group by name order by total_age ASC"""
    # fetch_query = """select Name,count(age) from person group by name"""
    cur.execute(fetch_query)
    result = cur.fetchall()
    print(result)
except sl.OperationalError as e:
    print(e)
except Exception as e:
    print(e)

conn.commit()
conn.close()