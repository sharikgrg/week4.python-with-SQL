import pyodbc
# In this file, we'll make our connection

# Parameters/variables for
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# Establish a connection
conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

cursor = conn_nwdb.cursor()
# Q1 - How many orders in NWDB?
order_count = cursor.execute("select count(OrderID) FROM Orders").fetchone()
print(order_count)

# Q2 - How many order that the Ship City is Rio de Janeiro?
order_count_rio = cursor.execute("select count(ShipCity) FROM Orders WHERE ShipCity = 'Rio de Janeiro'").fetchone()
print(order_count_rio)

# Q3 - Select all orders that the Ship City is Rio de Janeiro or Reims?
order_rio = cursor.execute("select * FROM Orders WHERE ShipCity = 'Rio de Janeiro' or ShipCity = 'Reims' ORDER by ShipCity")

while True:
    record = order_rio.fetchone()
    if record is None:
        break
    print(record)

# Q4 - Select all of the entries where the Company name has a z or a Z in the table of Customers
order_zcompany = cursor.execute("select * FROM Customers WHERE CompanyName like '%z%' or CompanyName like '%Z%' ")
while True:
    record = order_zcompany.fetchone()
    if record is None:
        break
    print(record.CompanyName)