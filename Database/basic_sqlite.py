import sqlite3

#Make Connection With Database
conn = sqlite3.connect("Bin.db")

#To Do Operations In Database We Need Cursor
c = conn.cursor()

#To Apply Execute Operations
# conn.execute()

#Create A Database Table 
c.execute(""" 
CREATE TABLE IF NOT EXIsTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER
)
 """)

# print("Executed Successfully")

#Enter Value In Table
c.execute(" INSERT INTO students (name,age) VALUES (?,?)", ('Aftab',20))
c.execute("SELECT * FROM students")
print(c.fetchall())
conn.commit
conn.close