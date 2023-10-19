from sqlalchemy import create_engine
import pandas as pd

# Connection parameters
server = 'YOUR_SERVER_NAME'
database = 'YOUR_DATABASE_NAME'
driver = '{ODBC Driver 17 for SQL Server}'  # or another driver if you're using something different

# Construct the connection string for SQL Server using a trusted connection
connection_string = f"mssql+pyodbc://{server}/{database}?trusted_connection=yes&driver={driver}"

engine = create_engine(connection_string)

# Fetch data using a SQL query (modify this to your needs)
sql_query = "SELECT * FROM your_table_name"
df = pd.read_sql(sql_query, engine)


# Replace this SQL query with your own
sql_query = "SELECT * FROM your_table_name"

# Use pandas to fetch data from the SQL query
df = pd.read_sql(sql_query, engine)
