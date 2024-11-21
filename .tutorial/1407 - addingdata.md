# 14-7. Adding Data to Tables

Once you have created a database file and created one or more tables, you can add rows to the table(s)

## a. Adding ONE row:
You can add a row using the **INSERT** statement.

**Syntax**:
`INSERT INTO TableName (ColumnName1, ColumnName2, etc...) VALUES (Value1, Value2, etc...)`

To insert a student row:  
```mysql
/* SQL Syntax */

INSERT INTO student 
(Name, CWID, major, phone, gpa) 
VALUES 
("John Smith", "100100", "HIST", "3182331111", 3.45)
```

<details>
  <summary>
    🔎 Closer Look:
  </summary>
  The column names do not have to be in the order they are designed<br>
They will be assigned values in the corresponding order they are specified<br>
If we had not provided values for any columns, they will be NULL at this moment<br>
According to our design, any field other than cwid can be empty<br>
We have not eclosed 3.45 in double quotes because we have defined it as REAL when we designed the table, so SQL is expecting a numeric data not a string
</details>


## b. Putting it in Python
The Python statement will be:  
```python
sql_stmt = '''
INSERT INTO student 
(Name, CWID, gpa) 
VALUES 
("John Smith", "100100", 3.45)
'''
cur.execute(sql_stmt)
```

<details>
  <summary>
    👉 Try this
  </summary>
  Write a Python statement to insert another row of data, use your own values
</details>


<details>
  <summary>
    👀 Answer
  </summary>

  ```python
  sql = ''' INSERT INTO student 
  (Name, major, phone, gpa, cwid) 
  VALUES 
  ("Mia Rose", "ACCT", "3180944343", 2.78, "100238")'''
  cur.execute(sql)
  ```
</details>

## c. Inserting multiple rows
We can add multiple rows in the same INSERT statement as follows: 
```python
sql_stmt = '''
INSERT INTO student (Name, gpa) 
VALUES 
("Jane Coyle", 3.45), 
("Peter Jones", 2.78),
("Mary Ruth", 3.45)
'''
cur.execute(sql_stmt)
```

<details>
  <summary>
    💡 Note:
  </summary>
  
  - We are not entering CWID, but Python will autoincrement
  - We are not entering other values for anyone here
  - Maybe we don't know the values at this point
  - So they are all going to be NULL
</details>

<details>
  <summary>
    👉 Try this
  </summary>
  Write a Python statement to insert two rows of data, use your own values using one insert statement
</details>


<details>
  <summary>
    👀 Answer
  </summary>

  ```python
  sql = ''' INSERT INTO student 
  (Name, major, phone, gpa)
  VALUES
  ("Millie Brown", "COSC", "3184541346", 3.2),
  ("Dean Wells", "CINS", "3188753876", 3.87)'''
  cur.execute(sql)
  ```
</details>

## d. Inserting NULL data
What if we know some major values  
How can we insert rows all in one INSERT statment with some having major and some not?  
We use the `NULL` keyword  

```python
sql_stmt = '''
INSERT INTO student 
(Name, Major, Phone) 
VALUES 
("Bethany Rhodes", NULL, "3183235678"), 
("Savannah Reese", "HIST", NULL), 
("Gabriel Webb", NULL, NULL)
'''

cur.execute(sql_stmt)
```

## e. Inserting values of variables
We have inserting strings or numbers so far  
But what if we have to insert variable values?  

### For example:  
```python
name = "Sammy Williams"    
gpa = 3.2
cwid = '100800'

parameter_tuple = (name, cwid, gpa)

sql_stmt = '''
INSERT INTO student 
(Name, CWID, gpa)
VALUES 
(?, ?, ?)
'''

cur.execute(sql_stmt, parameter_tuple)

```

<details>
  <summary>
    🔎 Closer Look:
  </summary>
  The VALUES clause has a tuple of question marks instead of values as the first argument<br>
  We are passing another tuple of variables as second argument to the execute method
</details>

<details>
  <summary>
    🚩 To Remember:
  </summary>
  This type of SQL statement is called parameterized query
</details>


<details>
  <summary>
    👉 Try this
  </summary>
  
  Insert the data from this dictionary into the student table  
  `student1 = {"name" : "Jimmy Rattigan",  
  "major" : "ACCT",  
  "gpa" : 2.1}`
  
</details>


<details>
  <summary>
    👀 Answer
  </summary>

  ```python
  name = student1["name"]
  major = student1["major"]
  gpa = student1["gpa"] 
  
  data_tuple = (name, major, gpa)
  
  sql = ''' INSERT INTO student
  (Name, major, gpa)
  VALUES 
  (?,?,?)'''
  cur.execute(sql, data_tuple)
  ```
</details>