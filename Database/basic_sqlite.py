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
c.executemany(" INSERT INTO students (name,age) VALUES (?,?)", 
[('Aftab',20),
('Omkar',24),
('Nishant',25),
('Nikhil',21),
('Ammar',19)
])
#To Search
c.execute("SELECT * FROM students WHERE name=?",("Aftab",))
#
c.execute("SELECT * FROM students WHERE name=?",("Aftab",))
items = c.fetchall()
for item in items:
    print(item)
conn.commit
conn.close
#Thanks 
