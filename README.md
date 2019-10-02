# Connecting SQL to Python using pyodbc

This is an example of us connecting to our sql server, using python and pyodbc.

We will look into :
- what is a cursor?
- Rows
- Querying the db
- Using while loops for efficient data queries
- Transactions

## Connection
        pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
        print(conn_nwdb)#
 Fill in the data in the code to connect the database with pycharm. It is a method imported from pyodbc
 
## .cursor()
The Cursor object represents a database cursor, which is typically used to manage the context of a fetch operation
- to create a new cursor: cnxn.commit()

## cursor().execute()

Prepares and executes SQL statement, returning the Cursor object itself

##.fetchall() VS .fetchone()
fetchall() returns all the remaining rows in the queries whereas fetchone() returns the first column of the first row if there are results.
- fetchall(), reads all the rows in a memory, so it could be problematic if there are a large amount of rows.

