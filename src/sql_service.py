import pyodbc
from fastapi import HTTPException
from .logger import logger

class SQLClient:

    def __init__(self, server, database, username, password):

        self.SERVER = server
        self.DATABASE = database
        self.USERNAME = username
        self.PASSWORD = password

    def get_conn(self):

        conn_str = (
            "DRIVER={ODBC Driver 18 for SQL Server};"
            f"SERVER={self.SERVER};"
            f"DATABASE={self.DATABASE};"
            f"UID={self.USERNAME};"
            f"PWD={self.PASSWORD};"
            "Encrypt=yes;"
            "TrustServerCertificate=no;"
            "Connection Timeout=30;"
        )

        try:
            conn = pyodbc.connect(conn_str)

            logger.info("SQL database connection successfully established \u2705")
            return conn

        except pyodbc.OperationalError:

            logger.error(f"Connection Failed due to invalid credentials \u274c")
            raise HTTPException(status_code=500, detail=f"Connection Failed: check the server credentials")

        except Exception as e:

            logger.error(f"Internal Server Error \u274c: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    
    
    def get_data(self, conn, sql_query):

        try:
            cursor = conn.cursor()
            cursor.execute(sql_query)

            columns = [column[0] for column in cursor.description]

            data = []

            for row in cursor.fetchall():
                data.append(dict(zip(columns, row)))

            logger.info("Successfully retrieved data from SQL database \u2705")

        except pyodbc.Error:

            logger.error(f"Database engine cannot perform a mathematically undefined operation \u274c")
            raise HTTPException(status_code=500, detail=f"Database engine cannot perform a mathematically undefined operation\n{str(e)}")

        except Exception as e:

            logger.error(f"Failed to retrieve data from server \u274c: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Failed to retrieve data from server\n{str(e)}")
        
        finally:
            logger.info("Closing the sql connection")
            conn.close()

        return data

