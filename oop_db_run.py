from oop_db_connect import *

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'


db_nw = ConnectMsS(server, database, username, password)
print(db_nw)
print(db_nw.conn_nwdb)

print(db_nw.cursor.execute("SELECT * FROM Products").fetchone())

print(db_nw.sql_query_fetchone("SELECT * FROM Products"))
print(db_nw.print_all_products_records('Products'))
print(db_nw.return_avg_price_products())