# 14-1. Intro to DB

## Database Management Systems
A Database Management System, or **DBMS** is a software that manages large collections of data  

### Popular DBMS Softwares
- MySQL
- Oracle
- MS SQL
- Postgres SQL
- SQLite

## History
File systems were orginally used to store and retrieve data  

But as the size of the data grew larger, simple operations like searching, inserting and deleting became cumbersome  

Hence, there was a need for DBMS which could store and manipulate large amounts of data in an organized and efficient manner

## SQL
- Structured Query Language **(SQL)** is a standard language for working with the DBMS
- Originally developed by IBM in 1970
- SQL consists of several keywords that you use to construct statements
- SQL statements are submitted to the DBMS, which are instructions to carry out operations on the data
- Python programs must construct these statments as strings and use a library method to pass these strings to the DBMS
  


## SQLite
- For this class we use SQLite
- It is easy to use
- Already comes installed with Python
- To use it just include the line of code `import sqlite3`