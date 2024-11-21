# 14-5. Opening and closing a Database Connection 

## a.
**Step 1:** Import the sqlite3 module  
```python
import sqlite3
```

## b.
**Step 2:** Connect to the database  
Connect to the database named students.db 

```python
conn = sqlite3.connect('students.db')
```
<details>
  <summary>
   🔎 Closer Look 
  </summary>
  A database is stored in a file on the system's disk<br> This step establishes a connection between the program and the database file<br>
  If db doesn't exist, it will be created<br>
  It will be an empty db with no tables<br>
</details>

## c.
**Step 3:** Get a cursor for the database  
A cursor is an object that is able to access and manipulate the data in a database.   
      
```python
cur = conn.cursor()
```

## d.
**Step 4:** Perform operations on the db  
Once you have the cursor, you can access and modify the data in the database as needed using the **execute** method 

```python
sql_str = ''   
cur.execute(sql_str)
```

<details>
  <summary>
   🔎 Closer Look 
  </summary>
  In the sql_str variable we will store the SQL statement to perform the operations on the database like retrieve data, add data, delete data etc<br>  
  Right now we have left sql_str empty, it will give an error if you execute with empty string 
</details>

## e.
**Step 5:** Commit changes to the database  
When you make changes to the database those changes aren't saved in the database until you commit those changes to the database.  

```python
conn.commit()
```

## f.
**Step 6:** Close the connection to the database  
When you are finished using the database you should close the connection  

```python
conn.close()
```
