USE Practica1;
GO

CREATE TABLE temp(
PassID NVARCHAR(6) PRIMARY KEY,
FName NVARCHAR(20),
LName NVARCHAR(20),
Gender NVARCHAR(6),
Age INT,
Nationality NVARCHAR(50),
AirportName NVARCHAR(50),
AirpotCountry NVARCHAR(6),
CountryName NVARCHAR(50),
AirportContinent NVARCHAR(6),
Continents NVARCHAR(50),
DepartureDate DATE,
ArrivalAirport NVARCHAR(6),
PilotName NVARCHAR(50),
FlightStatus NVARCHAR(50)
);
GO

SELECT * FROM temp;
GO