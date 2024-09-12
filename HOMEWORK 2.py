import sqlite3

from django.db.models.expressions import connector

conn = sqlite3.connect('name.db')
cursor = conn.cursor()
cursor.execute(''' CREATE TABLE emp ( ID PRIMARY KEY, NAME, EXPERIANCE, SALARY, AGE)''')
cursor.execute("INSERT INTO emp (ID, NAME, EXPERIANCE, SALARY, AGE) VALUES (357, 'ravi', 2, 100000,25)")
conn.commit()

cursor.execute("INSERT INTO emp (ID, NAME, EXPERIANCE, SALARY, AGE) VALUES (?,?, ?,?,?)", (468, 'vr', 4, 80000,26))
conn.commit()


cursor.execute("SELECT * FROM emp")
rows = cursor.fetchall()
for row in rows:
   print(row)


try:
    cursor.execute("SELECT * FROM non_existing_table")
except sqlite3.OperationalError as e:
   print(f"An error occurred: {e}")


cursor.close()
conn.close()
