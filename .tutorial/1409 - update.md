# 14-9. Updating and Deleting Existing Rows

## a. Updating row(s)
We use the UPDATE statement in SQL to change the value of an existing row.  
**Syntax:**  
```mysql
UPDATE <TableName> 
SET <ColumnName> = <DataValue> 
WHERE <Criteria>
```

### For example
To change the gpa of a student whose cwid is 100700 (from NULL) to 3.0  
```python
sql_stmt = '''
UPDATE student 
SET gpa = 3.0 
WHERE cwid = "100700" '''
cur.execute(sql_stmt)
```
<details>
  <summary>
    👉 14-9a Try this: 
  </summary>
  
  Write the above Update statement using a variable `cwid = 100700`
</details>


<details>
  <summary>
    👀 Answer:
  </summary>

  ```python
  cwid = 100700
  parameter_tuple = (cwid, )
  sql_stmt = '''
  UPDATE student 
  SET gpa = 3.0 
  WHERE cwid = ? '''
  cur.execute(sql_stmt, parameter_tuple)
  ```
</details>


## b. Using rowcount
To get the number of rows that were updated we can use the rowcount attribute  
### For example:
Let's set all the NULL gpa to 0 and see how many rows were affected 

```python
sql = ''' 
UPDATE student 
SET gpa = 0 
WHERE gpa IS NULL '''
cur.execute(sql)
print(cur.rowcount)
```

<details>
  <summary>
    👉 14-9b Try this: 
  </summary>

  Write the above update statement and if no rows are affected, print `Nothing was updated`
</details>


<details>
  <summary>
    👀 Answer:
  </summary>

```python
sql = '''UPDATE student 
SET gpa = 0 
WHERE gpa IS NULL'''
cur.execute(sql)
if cur.rowcount == 0:
  print("Nothing was updated")
  ```
</details>


## c. Deleting row(s)
We use the **DELETE** keyword to delete row(s) from a table  

**Syntax:**  
```mysql
DELETE FROM TableName WHERE Criteria
```
### For example:
To delete all the rows with gpa 0 

```python
sql = '''DELETE FROM student 
WHERE gpa = 0 '''
cur.execute(sql)  
print(cur.rowcount)
```


<details>
<summary>
  👉 14-9c Try this:
</summary>

  Write the above statement using the variable `gpa = 0`
</details>


<details>
<summary>
  👀 Answer:
</summary>

  ```python
  gpa = 0
  parameter_tuple = (gpa, )
  sql = '''DELETE FROM student 
  WHERE gpa = ? '''
  cur.execute(sql, parameter_tuple)  
  print(cur.rowcount)
  ```
</details>



<details>
  <summary>
    💡 Take Away:
  </summary>
  
  We have learned the CRUD operations in database programming using Python  
  
  C - Create db or table or rows/columns  
  R - Retrieve data from table  
  U - Update data in the table  
  D - Delete data from table/delete table
</details>