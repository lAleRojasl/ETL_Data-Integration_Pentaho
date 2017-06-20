SELECT ProductoID, SUM(Materiales.CostoUnitario*Cantidad) AS CostoMateriales
FROM MaterialXProducto
INNER JOIN Materiales ON Materiales.MaterialID = MaterialXProducto.MaterialID
GROUP BY ProductoID