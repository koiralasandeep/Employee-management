# 14-2. Tables, Rows and Columns

The data that is stored in a database is organized into one or more **tables**  
Each table holds a collection of relational data  
The data that is stored in a table is organized in rows and columns  

A **row** is a complete set of data about a single item, the data stored in a row is divided into columns  

Each **column** holds a sinlge piece of data about an item

|Name   	| Major  	| GPA  |  CWID  |
|----------------	|--------------	|---------------	| ----------- |
|John Smith   | HIST 	  |  2.45 	| 30010100 |
|  Jane Doe 	|  HIST 	|   	| 30010101 |
|  Mia Rose 	|  CINS 	|  3.27 	| 30010102 |
|  John Smith | COSC    |  3.42   | 30010103 |


## a. Column Data Types
When you create a database table, you must specify a data type for the columns
- These are NOT Python data types
- The data types are provided by the SQLite database
- Here is a table that lists the SQLite data types and the corresponding compatible Python data type

|SQLite Data Type   	| Description  	| Python Data type  |
|--------------------	|--------------	|------------------	|
|NULL   	| Unknown value  	|  None 	|
|  INTEGER 	|  Integer Number 	|   int	|
|  REAL 	|  Real Number 	|  float 	|
|  TEXT 	|  String 	|  str 	|
|  BLOB 	|  Binary Large Object 	|  Can be any object 	|

**NULL** can be used when the value is unknown or missing. When Python reads a NULL value into memory, the value is converted into None  

**INTEGER** holds a signed integer value (positive and negative numbers). When Python reads an INTEGER value into memory, the value is converted into int  

**REAL** holds a real number (with decimal places). When Python reads a REAL value into memory, the value is converted into float  

**TEXT** holds a string. When Python reads a TEXT value into memory, the value is converted into str  

**BLOB** holds an object of any type (for example, image or audio file). When Python reads a BLOB value into memory, the value is converted into a bytes object, which is an immutable sequence of bytes

