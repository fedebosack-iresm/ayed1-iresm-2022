'''
##**Ejercicio 5.5**
Crear una funcion que debe:

*   Pedir al usuario una cantidad de tramos de un viaje
*   Pedir al usuario la duracion en minutos de cada tramo (usar listas)
*   Calcular el tiempo total de viaje (motrar en horas)
*   No deben aparecer y se deben tener en cuenta todos los posibles errores
'''
import funciones_5_5 as f55
cant_tramos = f55.pedir_cantidad_tramos()
f55.calcular_suma(cant_tramos)