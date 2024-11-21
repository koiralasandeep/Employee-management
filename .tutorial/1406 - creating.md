# 14-6. Creating and Deleting Tables

## a. Creating a table
To create a table in a database, we use SQL statement **CREATE TABLE**  

**Syntax:**  
`CREATE TABLE <TableName> (<ColumnName1> <DataType1>, <ColumnName2> <DataType2>,<ColumnName3> <DataType3>, etc..)`  

For example, if you want to create a table `student` with four columns, this is how you can do it  

```mysql
/* SQL Syntax */
CREATE TABLE student (
  Name TEXT, 
  Major TEXT, 
  Phone TEXT, 
  gpa REAL)
```

<details>
  <summary>
    💡 Note:
  </summary>
  All the words in uppercase are SQL keywords<br>
  SQL is case-insensitive, but it is best practice to use upper case<br>
</details>


<details>
  <summary>
    🔎 Closer Look:
  </summary>
  The above statement will create a table with four columns<br>
  Name which is a string<br>
  Major which is a string<br>
  Phone which is a string<br>
  gpa which is a real number (or float as we call in Python)<br>
</details>


## b. Defining Primary Key      
You can also define a column named `cwid` as the primary key as shown below
```mysql
/* SQL Syntax */

CREATE TABLE student (
Name TEXT, 
Major TEXT, 
Phone TEXT,
gpa REAL,
cwid TEXT PRIMARY KEY)
```

When you define a primary key, it is a good practice to use the **NOT NULL** constraint.  
It specifies that the cwid column cannot be empty

```mysql
/* SQL Syntax */

CREATE TABLE student (
Name TEXT, 
Major TEXT, 
Phone TEXT,
gpa REAL,
cwid TEXT PRIMARY KEY NOT NULL)
```

## c. Auto-Incrementing Primary Key

If you do not want to enter the cwid but rather want the database to automatically increment it each time a new student is added, then you have to change its datatype to INTEGER

```mysql
/* SQL Syntax */

CREATE TABLE student (
Name TEXT, 
Major TEXT, 
Phone TEXT,
gpa REAL,
cwid INTEGER PRIMARY KEY NOT NULL)
```

## d. Creating Table Using IF NOT EXISTS
An error will occur if you try to create a table that already exists.  
To prevent the error, you can use the keywords IF NOT EXISTS  
```mysql
/* SQL Syntax */

CREATE TABLE IF NOT EXISTS student (
Name TEXT, 
Major TEXT, 
Phone TEXT,
gpa REAL,
cwid INTEGER PRIMARY KEY NOT NULL)
```

## e. Putting it in Python

To execute our statement above in Python, we must pass it as a string as shown below:

```python
sql_str = '''
CREATE TABLE IF NOT EXISTS 
student (
Name TEXT, 
Major TEXT, 
Phone TEXT, 
gpa REAL, 
cwid INTEGER PRIMARY KEY NOT NULL)
'''

cur.execute(sql_str)
```

## f. Deleting a table
To delete an existing table we use the keyword **DROP TABLE**  

**Syntax:**  
`DROP TABLE <TableName>`

To delete the student table, the SQL statement would be:
```mysql
/* SQL Syntax */

DROP TABLE student
```

## g. Deleting a table using IF EXISTS
  
The above statement will give an error if the table doesn't exist, so to prevent the error, we use **IF EXISTS**  

```mysql
/* SQL Syntax */

DROP TABLE IF EXISTS <TableName>
```

## 6h. Putting it in Python
To delete a table named student without raising an exception

```python
sql = '''DROP TABLE IF EXISTS student'''
cur.execute(sql)
```
