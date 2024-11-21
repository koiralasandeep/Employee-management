
```python
import sqlite3
conn = sqlite3.connect('students.db')
cur = conn.cursor()
sql_str = '''
CREATE TABLE IF NOT EXISTS 
student (
Name TEXT, 
Major TEXT, 
Phone TEXT, 
gpa REAL, 
cwid INTEGER PRIMARY KEY NOT NULL)
'''

sql = '''SELECT * FROM student'''
cur.execute(sql)
rows = cur.fetchall()
for row in rows:
  new_row = ['' if data is None else data for data in row]
  print(f'{new_row[4] : ^4} | {new_row[0] : <15} | {new_row[1] : ^6} | {new_row[2] : ^12} | {new_row[3] : >6} |')


conn.commit()
conn.close()
```

  