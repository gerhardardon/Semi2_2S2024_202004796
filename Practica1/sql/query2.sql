USE Practica1;

SELECT 
    Gender, 
    COUNT(*) AS Cant,
    (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Pasenger)) AS Porcentaje
FROM 
    Pasenger
GROUP BY 
    Gender;
