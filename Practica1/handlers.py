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
    print("-extraccion exitosa")

    # Limpiar data
    # Eliminar duplicados
    clean_data_command = """
        WITH CTE AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY PassID ORDER BY (SELECT NULL)) AS rn
    FROM Passengers
    )
    DELETE FROM CTE
    WHERE rn > 1;
    """

    # Eliminar null
    clean_data_command = """
        DELETE FROM temp
        WHERE PassID IS NULL OR FName IS NULL OR LName IS NULL OR Gender IS NULL OR Age IS NULL OR Nationality IS NULL OR AirportName IS NULL OR AirportCountry IS NULL OR CountryName IS NULL OR AirportContinent IS NULL OR Continents IS NULL OR DepartureDate IS NULL OR ArrivalAirport IS NULL OR Pilotname IS NULL OR FlightStatus IS NULL
    """
    cursor.execute(clean_data_command)
    conn.commit()
    print("-limpieza exitosa")

    cursor.close()
    conn.close()
    
