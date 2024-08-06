import pyodbc

SERVER = 'localhost'
DATABASE = 'Practica1'
USERNAME = 'SA'
PASSWORD = 'Gerhard556@'


def connect():
    connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
    try:
        with pyodbc.connect(connectionString) as conn:
            return conn
    except Exception as e:
        print(f'Error: {e}')
        return None


def extraer(path):
    conn = connect()
    cursor = conn.cursor()
    # Bulk insert
    bulk_insert_command = """
        BULK INSERT temp
        FROM '/var/opt/mssql/data/data.csv'
        WITH (
            FIELDTERMINATOR = ',',
            ROWTERMINATOR = '\\n',
            FIRSTROW = 2
        );
        """
    cursor.execute(bulk_insert_command)
    conn.commit()
    cursor.close()
    conn.close()
    print("-extraccion exitosa")
