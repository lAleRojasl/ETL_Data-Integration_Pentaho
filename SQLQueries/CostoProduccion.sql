USE InventariosDBReplication

SELECT Nombre as Producto, Modelo, CostoMateriales, PrecioVenta
FROM
(
SELECT ProductoID, SUM(Materiales.CostoUnitario*Cantidad) AS CostoMateriales
FROM MaterialXProducto
INNER JOIN Materiales ON Materiales.MaterialID = MaterialXProducto.MaterialID
GROUP BY ProductoID
) AS CostoProd
INNER JOIN VentasDB.dbo.Productos ON VentasDB.dbo.Productos.ProductoID = CostoProd.ProductoID