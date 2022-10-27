'''
###**Ejercicio 6.1**
Crear una clase de Persona:
*   Cuyo constructutor debe inicializar los atributos nombre, apellido, edad, ciudad_de_recidencia
*   Se deben crear dos metodos en la clase:
    1.  Presentarse que la persona indique: Soy {nombre} {apellido}, tengo {edad} años y vivo en {ciudad de recidencia}
    2.  Indique segun la edad de la persona si esta es: Niño (0 a 14), Adolecente (14 a 22), Joven (22 a 30), mayor(30 a 50), mas mayor(50 a 120)
    
Crear una funcion que permita agregar objectos a una lista
'''
import Persona as pe
lista_personas = []

def creador_de_personas(lista_personas):
    while True:
        nombre = input('Ingrese el nombre de la persona (exit para salir): ')
        if(nombre == 'exit'):
            break
        apellido = input('Ingrese el apellido de la persona: ')
        edad = int(input('Ingrese la edad de la persona: '))
        residencia = input('Ingrese la residencia de la persona: ')

        persona = pe.Persona(nombre,apellido,edad,residencia)
        lista_personas.append(persona)

def recorrer_lista_personas(lista_personas):
    for per in lista_personas:
        per.presentarse()
        per.get_edad()

creador_de_personas(lista_personas)
recorrer_lista_personas(lista_personas)