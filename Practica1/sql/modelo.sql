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

GO