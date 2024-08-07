USE Practica1;

SELECT TOP 5
    p.Age AS Age,
    p.Gender AS Gender,
    COUNT(h.PassID) AS Count
    FROM 
        Hechos h
    JOIN
        Pasenger p ON h.PassID = p.PassID   
    GROUP BY
        p.Age, 
        p.Gender  
    ORDER BY
        Count DESC;
