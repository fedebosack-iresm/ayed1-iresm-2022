'''
###**Ejercicio 6.3**
Crear una clase de Peliculas:
*   Cuyo constructutor debe inicializar los atributos nombre, año, genero, nacionalidad, puntuacion
*   Se deben crear 4 metodos en la clase:
    1.  Presentar la pelicula: La pelicula {nombre} de {genero} del {año} obtuvo una puntuacion de {puntuacion}  y fue filmada en {nacionalidad}
    2.  Retornar si el año de la pelicula es mayor o igual o menor al pasado por parametro
    3. Cambiar el genero de una pelicula
    4. Modificar puntuacion de la pelicula (entre 1 y 10)

El programa debe:
*   Tener un menu con 4 opciones: (GestorPeliculas)
    1. Crear una pelicula y guardar su nombre en una lista de peliculas.
    2. Verificar si la pelicula deseada existe en la lista de peliculas.
    3. Pedir a la lista de peliculas, todas las de un año.
    4. Presentar una pelicula de la lista
    5. Cambiar el genero de una pelicula'''

import gestorpeliculas as gp

gestor = gp.GestorPeliculas()
while True:
    menu ='''
1.Crear una pelicula y guardar su nombre en una lista de peliculas.
2.Verificar si la pelicula deseada existe en la lista de peliculas.
3.Pedir a la lista de peliculas, todas las de un año.
4.Presentar una pelicula de la lista
5.Cambiar el genero de una pelicula
6.salir
Ingrese una opcion: '''
    opcion = input(menu)
    if(opcion == '1'):
        gestor.crear_pelicula()
    elif(opcion == '2'):
        pelicula = input('Ingrse la pelicula deseada: ')
        gestor.verificar_pelicula(pelicula)
    elif(opcion == '3'):
        anio_verificar = int(input('Ingrse el año a verificar: '))
        gestor.verificar_peliculas_anio(anio_verificar)
    elif(opcion == '4'):
        gestor.presentar_peliculas()
    elif(opcion == '5'):
        pelicula = input('Ingrse la pelicula deseada: ')
        genero = input('Ingrse el nuevo genero: ')
        gestor.cambiar_genero(pelicula,genero)
    elif(opcion == '6'):
        exit()            
    else:
        print('Opcion incorrecta')
