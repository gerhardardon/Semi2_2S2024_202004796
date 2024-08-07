USE Practica1;

SELECT 
    FORMAT(f.DepartureDate, 'MM-yyyy') AS Fecha, 
    COUNT(*) AS Count
FROM 
    Flight f
GROUP BY 
    FORMAT(f.DepartureDate, 'MM-yyyy')
ORDER BY 
    FORMAT(f.DepartureDate, 'MM-yyyy');
