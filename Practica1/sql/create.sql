USE Practica1;
GO

CREATE TABLE temp(
PassID NVARCHAR(6),
FName NVARCHAR(120),
LName NVARCHAR(120),
Gender NVARCHAR(6),
Age INT,
Nationality NVARCHAR(150),
AirportName NVARCHAR(150),
AirportCountry NVARCHAR(6),
CountryName NVARCHAR(150),
AirportContinent NVARCHAR(6),
Continents NVARCHAR(150),
DepartureDate DATE,
ArrivalAirport NVARCHAR(6),
PilotName NVARCHAR(150),
FlightStatus NVARCHAR(150)
);
GO

SELECT * FROM temp;
GO