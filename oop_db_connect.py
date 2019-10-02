import pyodbc

# concept of 'Strong Prams'
    # never ever trust user input
    # avoid SQL injections
    # filter for SQL injections

class ConnectMsS():

    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.conn_nwdb.cursor()

    def __filter_query(self,query):
        # Doing some filtering for bad queries
        return self.cursor.execute(query)

    def sql_query(self,query):
        return self.__filter_query(query)

    def sql_query_fetchone(self, query):
        return self.__filter_query(query).fetchone()

    def print_all_products_records(self, table):
        query_rows = self.__filter_query(f"SELECT * FROM {table}")
        while True:
            record = query_rows.fetchone()
            if record is None:
                break
            return record

    def return_avg_price_products(self):
        query = self.__filter_query("SELECT * FROM Products")
        prices = []

        while True:
            #get individual prices and append to my list
            record = query.fetchone()
            if record is None:
                break
            prices.append(record.UnitPrice)
        return sum(prices)/len(prices)


    # CRUD

    # Create 1 entry
        # use Insert
        # the cursor cannot make transaction ( go to documentation)
    

    # Read all entries
        # Fetch all record and return as a list of dictionaries
    def read_all_entries(self, table):
        query_rows = self.__filter_query(f"SELECT * FROM {table}")
        while True:
            record = query_rows.fetchone()
            if record is None:
                break
            return record

    # Read one entry
        # Fetch specific record
        # Get one value using ID
    def read_one_entry(self, table, ID, number): # table to specify table, ID to specify which ID, number to specify which number
        query = self.__filter_query(f"SELECT * FROM {table} WHERE {ID} = {int(number)}")
        return query.fetchone()


    # Update 1 entry
        # the ID of the record to update
        # update the specific record
            # the cursor cannot make transaction( go to documentation)
    # Update 1 entry

    # Destroy / 1 entry
        # THE ID OF the specific record
        # Destroythe record
            # the cursor cannot make transaction( go to documentation)