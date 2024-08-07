USE Practica1;
SELECT 
    c.CountryName, 
    YEAR(f.DepartureDate) AS Year, 
    MONTH(f.DepartureDate) AS Month, 
    COUNT(*) AS TripCount
FROM 
    Hechos h
JOIN 
    Country c ON h.CountryID = c.CountryID
JOIN 
    Flight f ON h.FlightID = f.FlightID
GROUP BY 
    c.CountryName, 
    YEAR(f.DepartureDate), 
    MONTH(f.DepartureDate)
ORDER BY 
    c.CountryName, 
    Year, 
    Month;
