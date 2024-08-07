USE Practica1;

SELECT TOP 5
    c.Continents AS Continent,
    COUNT(h.PassID) AS Count
    FROM 
        Hechos h
    JOIN
        Continent c ON h.ContinentID = c.ContinentID
    GROUP BY
        c.Continents
    ORDER BY
        Count DESC;
        