USE InventariosDBReplication

SELECT Nombre, Modelo, TotalEntradas+TotalSalidas as TotalMovimientos
FROM
(
	SELECT TOP(50) Entradas.MaterialID, TotalEntradas, TotalSalidas FROM
	(
	SELECT MaterialID, SUM(Cantidad) as TotalEntradas FROM
	(
		SELECT OrdenID, MaterialID, Cantidad
		FROM LineasXOrden
		) AS Lineas
		INNER JOIN OrdenDeCompra ON OrdenDeCompra.OrdenID = Lineas.OrdenID
		WHERE OrdenDeCompra.TotalCancelado != 0
		GROUP BY MaterialID
		) AS Entradas
	INNER JOIN
	(
	SELECT MaterialID, SUM(Cantidad) as TotalSalidas
	FROM MovSalidas
	GROUP BY MaterialID
	) AS Salidas
	ON Entradas.MaterialID = Salidas.MaterialID
	) AS TotalMovimientos
INNER JOIN Materiales ON Materiales.MaterialID = TotalMovimientos.MaterialID 
ORDER BY TotalMovimientos DESC