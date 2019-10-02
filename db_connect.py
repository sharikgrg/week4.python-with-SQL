import pyodbc
# In this file, we'll make our connection

# Parameters/variables for
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# Establish a connection
conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
print(conn_nwdb)

# Create a cursor
# allows us to execute read only queries
cursor = conn_nwdb.cursor()
# using .execute on cursor
cursor.execute("SELECT * FROM customers")

# Fetch rows from cursor - .fetchone
row = cursor.fetchone()
print(row.ContactName)

row = cursor.fetchone() # It maintains state
print(row.ContactName)

row = cursor.fetchone() # it maintains state
print(row.ContactName)

# print(row)

# .fetchall()

row = cursor.execute("SELECT * FROM Customers").fetchall()
# WE can iterate
# We don't you this mm'kay....
# for row in row:
#     print(row)
print(len(row))
print(type(row)) #This is a list, then:

# row = cursor.execute("SELECT * FROM Products").fetchall()
# for record in row:
#     print(type(record))
#     print(record.UnitPrice)  # We can access the columns of a specific records

#However, this is dangerous.
# AS it can clog our machine with too much data
    # We can use while loop to be more efficient

# row = cursor.execute("SELECT * FROM Products")
#
# while True:
#     record = row.fetchone()
#     if record is None:
#         break
#     print(record.UnitPrice)