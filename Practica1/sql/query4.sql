USE Practica1;
SELECT 
    c.CountryName, 
    COUNT(*) AS Count
FROM 
    Hechos h
JOIN 
    Country c ON h.CountryID = c.CountryID
JOIN 
    Flight f ON h.FlightID = f.FlightID
GROUP BY 
    c.CountryName
ORDER BY 
    Count DESC;
