USE Practica1;
SELECT TOP 5 
    a.AirportName, 
    COUNT(p.PassID) AS Count
FROM 
    Hechos h
JOIN 
    Airport a ON h.AirportID = a.AirportID
JOIN 
    Pasenger p ON h.PassID = p.PassID
GROUP BY 
    a.AirportName
ORDER BY 
    Count DESC;
