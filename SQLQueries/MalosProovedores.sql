USE InventariosDBReplication


SELECT Nombre, Estado, Ocasiones
FROM 
(
SELECT DistribuidorID, Estado, COUNT(OrdenID) as Ocasiones
FROM OrdenDeCompra
WHERE Estado != 'Recibido'
GROUP BY DistribuidorID, Estado
) AS EstadosOrden
INNER JOIN 
Distribuidores ON Distribuidores.DistribuidorID = EstadosOrden.DistribuidorID
ORDER BY Ocasiones DESC, Nombre ASC
