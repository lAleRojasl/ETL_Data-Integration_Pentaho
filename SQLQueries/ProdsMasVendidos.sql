USE VentasDB

SELECT Nombre, Modelo, Vendidos
FROM
(
SELECT ProductoID, COUNT(VentaID) as Vendidos
FROM VentasXCliente
GROUP BY ProductoID) AS VentasProd
INNER JOIN
Productos ON Productos.ProductoID = VentasProd.ProductoID