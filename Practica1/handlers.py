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
    FROM temp
    )
    DELETE FROM CTE
    WHERE rn > 1;
    """

    # Eliminar null
    clean_data_command2 = """
        DELETE FROM temp
        WHERE PassID IS NULL OR FName IS NULL OR LName IS NULL OR Gender IS NULL OR Age IS NULL OR Nationality IS NULL OR AirportName IS NULL OR AirportCountry IS NULL OR CountryName IS NULL OR AirportContinent IS NULL OR Continents IS NULL OR DepartureDate IS NULL OR ArrivalAirport IS NULL OR Pilotname IS NULL OR FlightStatus IS NULL
    """

    # Setear mayusculas 
    clean_data_command3 = """
        UPDATE temp
        SET AirportContinent = upper(AirportContinent),
        ArrivalAirport = upper(ArrivalAirport)
    """

    cursor.execute(clean_data_command)
    cursor.execute(clean_data_command2)
    cursor.execute(clean_data_command3)
    conn.commit()
    print("-limpieza exitosa")

    cursor.close()
    conn.close()
    
def borrar():
    conn = connect()
    cursor = conn.cursor()
    # Borrar tabla
    drop_table_command = """
        USE Practica1;
        DROP TABLE Hechos;
        DROP TABLE Pasenger;
        DROP TABLE Airport;
        DROP TABLE Country;
        DROP TABLE Continent;
        DROP TABLE Flight;
    """
    cursor.execute(drop_table_command)
    conn.commit()
    print("-borrado exitoso")
    cursor.close()
    conn.close()

def crear():
    conn = connect()
    cursor = conn.cursor()
    # Crear tablas
    create_table_command = """
    USE Practica1;

    CREATE TABLE Pasenger(
        PassID NVARCHAR(6) PRIMARY KEY,
        FName NVARCHAR(120),
        LName NVARCHAR(120),
        Gender NVARCHAR(6),
        Age INT,
        Nationality NVARCHAR(150)
    );

    CREATE TABLE Airport(
        AirportID INT IDENTITY(1,1) PRIMARY KEY,
        AirportName NVARCHAR(150)
    );

    CREATE TABLE Country(
        CountryID INT IDENTITY(1,1) PRIMARY KEY,
        AirportCountry NVARCHAR(6),
        CountryName NVARCHAR(150)
    );

    CREATE TABLE Continent(
        ContinentID INT IDENTITY(1,1) PRIMARY KEY,
        AirportContinent NVARCHAR(6),
        Continents NVARCHAR(150)
    );

    CREATE TABLE Flight(
        FlightID INT IDENTITY(1,1) PRIMARY KEY,
        DepartureDate DATE,
        ArrivalAirport NVARCHAR(6),
        PilotName NVARCHAR(150),
        FlightStatus NVARCHAR(150)
    );

    CREATE TABLE Hechos(
        PassID NVARCHAR(6),
        AirportID INT,
        CountryID INT,
        ContinentID INT,
        FlightID INT, 
        FOREIGN KEY (PassID) REFERENCES Pasenger(PassID),
        FOREIGN KEY (AirportID) REFERENCES Airport(AirportID),
        FOREIGN KEY (CountryID) REFERENCES Country(CountryID),
        FOREIGN KEY (ContinentID) REFERENCES Continent(ContinentID),
        FOREIGN KEY (FlightID) REFERENCES Flight(FlightID)
    );
    """
    cursor.execute(create_table_command)
    conn.commit()
    print("-creacion exitosa")
    cursor.close()

def cargar():
    conn = connect()
    cursor = conn.cursor()

    # Llenar tablas de Dimensiones 
    fill_table_command = """
    INSERT INTO Pasenger(PassID, FName, LName, Gender, Age, Nationality)
    SELECT DISTINCT PassID, FName, LName, Gender, Age, Nationality
    FROM temp;

    INSERT INTO Airport(AirportName)
    SELECT DISTINCT AirportName
    FROM temp;

    INSERT INTO Country(AirportCountry, CountryName)
    SELECT DISTINCT AirportCountry, CountryName
    FROM temp;

    INSERT INTO Continent(AirportContinent, Continents)
    SELECT DISTINCT AirportContinent, Continents
    FROM temp;

    INSERT INTO Flight(DepartureDate, ArrivalAirport, PilotName, FlightStatus)
    SELECT DISTINCT DepartureDate, ArrivalAirport, PilotName, FlightStatus
    FROM temp;
    """
    # Llenar tabla de Hechos
    

    cursor.execute(fill_table_command)
    conn.commit()
    print("-carga exitosa")
    cursor.close()
    conn.close()
