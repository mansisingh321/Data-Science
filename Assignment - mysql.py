#############       ASSIGNMENT - MySQL 

""" 
Que 1: What is a database? Differentiate between SQL and NoSQL databases.

Ans :  A dataset is a structured collection of data organized for efficient storage, retrieval, and management. It allow users and applications to interact with the data in a structured and organized manner.
SQL Database: Suitable for structured data and scenarios where data consistency is paramount, In sql data is stored in tables with predefined schemas.
NoSQL Database: Thay are more versatile for handling various data types or data models like document, keyvalue, graphs. They offer more flexible and dynamic schemas, allowing for schema evolution.


Que2 : What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.

Ans :  DDL : Stands for Data Definition Language. It is a subset of SQL used to define and manage the structure of a database, including creating, modifying, and deleting database objects such as tables, indexes and constraints.
CREATE : This is used to create new database objects, such as tables, views, indexes and more. 
DROP : Used to remove existing database objects, such as tables, views or indexes.
ALTER : Used to modify existing database objects. It can be used to add, modify or delete columns, constraints and other attributes of an object.
TRUNCATE : Used to remove all the data from a table, but unlike DROP statement it retains the table structure for further use.

Que3 : What is DML? Explain INSERT, UPDATE, and DELETE with an example.

Ans : DML stands for Data Manipulation Language. It is a subset of SQL used to interact with the data stored in a database.
INSERT : Used to add new rows of data into a table. It specifies the table's name and the values to be inserted into the corresponding columns
UPDATE : Used to modify existing data within a table. Specifies which rows to update and the new values to be set for specific columns.
DELETE : Used to remove rows from a table based on specified conditions.

Que4 : What is DQL? Explain SELECT with an example.

Ans : DQL : Stands for Data Query Language. It is a subest of SQL used to retrieve and query data from a database.
SELECT : It is used to retrieve data from one or more tables. It allows you to specify the columns you want to retrieve, the table or tables from which to retrieve the data, and optional filtering conditions.


Que5 : Explain Primary Key and Foreign Key.

Ans : Primary Key : Primary key is a column or sets of columns in a database that uniquely identifies each row or record in that table
Foreign Key :  A foreign key is a column in a table that establishes a link between the data in two tables. It creates a relationship between the tables by refrencing the primary key of another variable.

Que 6 : Write a python code to connect MySQL to python. Explain the cursor() and execute() method.
Ans 6 :
"""
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

# cursor() : This method is used to create a cursor object that enables to interact with the database. The cursor acts as a control structure that allow us to execute SQL queries and fetch results.
# execute() : This is used to execute the SQL queries through the cursor. It takes an sql query string as an argument and executes it within the database. 

"""
Que 7 : Give the order of execution of SQL clauses in an SQL query.

Ans 7 : SQL clauses are specific keywords or phrases used in SQL to define various aspects of a query. Helps to retrieve, and manage data stored in a database.

1. SELECT : Specifies which columns to retreive from the table.
2. FROM : Specifies the table(s) from which we retrieve the data.
3. JOIN : Combines data from multiple tables based on specified conditions.
4. WHERE : Filters rows based on specified conditions.
5. GROUP BY : Groups rows with smiliar values in specified columns.
6. HAVING : Filters grouped data based on specified conditions.
7. ORDER BY : Sorts the result set based on specified solumns and sorting directions.
8. LIMIT/OFFSET : Limits the number of rows returned nd skips a certain number of rows.
"""

