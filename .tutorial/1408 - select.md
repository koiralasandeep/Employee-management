# 14-8. Querying Database with Select Statement
Now our table has some data.  
How do we retrieve all or some of the data?

## a. Selecting all columns in a table
We use the SELECT statement in the following general format:  
```mysql
/* SQL Syntax */

SELECT * FROM <TableName>
```

<details>
  <summary>
    🔎 Closer Look:
  </summary>
  * selects all the columns and all the rows<br>
  You can specify a certain column or columns if you don't need all the columns
</details>

To get all the data from our student table, we write the following Python statement:

```python
sql_stmt = '''
SELECT * FROM student
'''
cur.execute(sql_stmt)

# We use fetchall method to get values
rows = cur.fetchall()

# Printing the retrieved values
suchi_print(rows) 

```

<details>
  <summary>
    🚩 To Remember:
  </summary>
  fetchall method returns a list of tuples
</details>

<details>
  <summary>
    👉 14-8a Try this:
  </summary>
  From the above select statement, print data returned bu fetchall in a tabular format, choose alignment and widths to fit the data
</details>


<details>
  <summary>
    👀 Answer:
  </summary>

  ```python
  rows = cur.fetchall()
  for row in rows:
    
    # replace any None values with blank strings
    
    if row[0] is not None:
      name = row[0]
    else:
      name = ''

    if row[1] is not None:
      major = row[1]
    else:
      major = ''

    if row[2] is not None:
      phone = row[2]
    else:
      phone = ''

    if row[3] is not None:
      gpa = row[3]
    else:
      gpa = ''

    cwid = row[4]

    print(f'{cwid: ^6} | {name : <15} | {major : ^6} | {phone : ^12} | {gpa : >6} |')


    
  
  ```

  Another way of doing this using list comprehension

  ```python
  rows = cur.fetchall()
  for row in rows:
    new_row = ['' if data is None else data for data in row] # create a new list to replace all None values with blank strings
    print(f'{new_row[4] : ^4} | {new_row[0] : <15} | {new_row[1] : ^6} | {new_row[2] : ^12} | {new_row[3] : >6} |')
  ```
</details>

## b. Selecting specified columns
To only select the cwid and gpa, we can write the following statement:  
```python
sql = '''SELECT cwid, gpa FROM student'''
cur.execute(sql)
rows = cur.fetchall()
suchi_print(rows)

# Or use for loop
```

<details>
  <summary>
    🔎 Closer Look:
  </summary>
  This select statement will retrieve only two columns, but all the rows in the table
</details>

## c. Selecting using WHERE clause
If you wanted to retrieve only the rows that fit a specific criteria, you can do that using the **WHERE** keyword.  

### For example
If you wanted to see which students have GPA >= 3.5, the statment would be

```python
sql_stmt = '''SELECT CWID, gpa WHERE gpa >= 3.5'''
cur.execute(sql_stmt)
rows = cur.fetchall()
suchi_print(rows)
```

## d. Parameterized Select Query using WHERE clause 
What if the gpa value is stored in a variable?  
We use parameterized query  

```python
gpa_val = 3.5
data_tuple = (gpa_val, )
sql_stmt = '''SELECT CWID, gpa 
FROM student 
WHERE gpa >= ?'''
cur.execute(sql_stmt, data_tuple)

rows = cur.fetchall()
suchi_print(rows)
```

<details>
  <summary>
    💡 Note:
  </summary>
  In the WHERE clause we can use <br>
  relational operators (<, >, =, ==, !=, >=, <=, <>) or <br>
    logical operators (AND, OR, NOT) or<br>
    LIKE operator
</details>


## e. Sorting the results of SELECT statement
We can use **ORDER BY** to sort the results 
```python
sql_stmt = '''
SELECT cwid, gpa 
FROM student 
ORDER BY cwid ASC'''
cur.execute(sql_stmt)

rows = cur.fetchall()
suchi_print(rows)
```

<details>
  <summary>
    💡 Note:
  </summary>
    The above statement will sort the results by ascending order of CWID<br>
    To sort by descending we use the DESC keyword
</details>
    
## 8f. Aggregate Functions
In SQL, an aggregate function performs a calculation on a set of values from a table and returns a single value.

### For example
If we want to calculate the average GPA of all the students in the student table, we will use AVG function  
```python
sql_stmt = '''SELECT AVG(gpa) FROM student'''
cur.execute(sql_stmt) 
row = cur.fetchone()
suchi_print(row)
```

<details>
  <summary>
    🔎 Closer Look:
  </summary>
  We are using fetchone, because we know only one row will be returned
</details>


<details>
  <summary>
    💡 Note:
  </summary>
  Other aggregate functions are SUM, MIN, MAX and COUNT
</details>