'''
###**Ejercicio 6.2**
Crear una clase de FiguraGeometrica:
*   Cuyo constructutor debe inicializar los atributos tipo_de_figura, color, y tamaño (por defecto "pequeño")
*   Se deben crear 3 metodos en la clase:
    1.  Presentar la figura: Un {tipo_de_figura} de color {color} y tamaño {tamaño}
    2.  Cambiar color de figura e indicar nuevo color
    3.  verificar si la figura es tamaño pequeño, agrandar a tamaño grande
'''

import FiguraGeometrica as fg
lista_figuras = []

def creador_de_figuras(lista_figuras):
    while True:
        tipo = input('Ingrese el tipo de figura (exit para salir): ')
        if(tipo == 'exit'):
            break
        color = input('Ingrese el color de la figura: ')
        tamanio = input('Ingrese el tamnio de la figura: ')

        figura = fg.FiguraGeometrica(tipo,color,tamanio)
        lista_figuras.append(figura)

def recorrer_lista_figuras(lista_figuras):
    for fig in lista_figuras:
        fig.presentarse()

creador_de_figuras(lista_figuras)
recorrer_lista_figuras(lista_figuras)