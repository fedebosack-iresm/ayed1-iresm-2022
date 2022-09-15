"""
##**Ejercicio 4.6 (Programa de ventas)**
El programa debe:
*   Simular un programa que venda 3 productos

Codigo   Nombre    Precio  Stock
1   &   producto1   & 300 & 5
2   &   producto2   & 400 & 4
3   &   producto3   & 500 & 7

*   El menu debe mostrar los productos a comprar.
*   Luego se debe contar con un menu de si se pagara en efectivo o tarjeta credito o debito
*   Contar con 7 funciones:
  1.  Ver menu de productos
  2.  Pagar con tarjeta credito (Se debe cobrar 10% mas y se debe descontar el stock)
  3.  Pagar con tarjeta debito (se debe descontar el stock)
  4.  Pagar con efectivo (Se debe cobrar 10% menos y se debe descontar el stock)
  5.  consultar productos y stock
  6.  agregar stock a los productos
  7.  cambiar el precio a los productos
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
"""
import funciones_4_6 as fu_4_6

fu_4_6.menu()