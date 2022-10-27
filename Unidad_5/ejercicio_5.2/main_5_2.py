'''
##**Ejercicio 5.1**
Crear una funcion que debe: (usar listas)

*    Pedir al usuario cantidad de personas
*    Pedir al usuario una a una la edad de las personas
*    Finalizado la carga de las edades debe imprimir por pantalla la edad mayor
*    No deben aparecer y se deben tener en cuenta todos los posibles errores
'''
import funciones_5_2 as f52
cant_personas = f52.pedir_cantidad()
f52.cargar_edades(cant_personas)