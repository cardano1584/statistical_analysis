import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

class DataRetriever:
    # Class-level attribute to store the engine
    _engine = None
    
    @classmethod
    def set_engine(cls, connection_string):
        """Set engine for the class"""
        cls._engine = create_engine(connection_string)

    def __init__(self, sql_query):
        self.sql_query = sql_query
        self.data = None  # Will hold the pandas DataFrame
        self._fetch_data()

    def _fetch_data(self):
        """Fetch data using the provided SQL query"""
        try:
            self.data = pd.read_sql(self.sql_query, self._engine)
        except SQLAlchemyError as e:  # Capture only SQLAlchemy related errors
            self._log_error(str(e))

    def _log_error(self, error_message):
        """Log errors to a table in the database"""
        error_log_query = text("""
            INSERT INTO ##ErrorLog (ErrorMessage)
            VALUES (:error_message)
        """)

        # Use the engine to execute the insert
        with self._engine.connect() as connection:
            connection.execute(error_log_query, params={"error_message": error_message})

# Example usage:
# Set up the engine first
DataRetriever.set_engine("mssql+pyodbc://server/database?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes")

# Initialize an instance with an SQL query
instance = DataRetriever("SELECT * FROM some_table")

# Access the data
print(instance.data)


"""
CREATE TABLE ##ErrorLog
(
    ID INT IDENTITY(1,1) PRIMARY KEY,
    ErrorMessage NVARCHAR(MAX),
    ErrorTime DATETIME DEFAULT GETDATE()
);

"""