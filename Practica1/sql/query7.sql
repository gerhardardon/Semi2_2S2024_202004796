USE Practica1;

SELECT TOP 5
    c.CountryName,
    COUNT(h.PassID) AS Count
    FROM 
        Hechos h
    JOIN
        Country c ON h.CountryID = c.CountryID
    GROUP BY
        c.CountryName
    ORDER BY
        Count DESC;

