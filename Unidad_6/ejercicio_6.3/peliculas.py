'''
###**Ejercicio 6.3**
Crear una clase de Peliculas:
*   Cuyo constructutor debe inicializar los atributos nombre, año, genero, nacionalidad, puntuacion
*   Se deben crear 4 metodos en la clase:
    1. Presentar la pelicula: La pelicula {nombre} de {genero} del {año} obtuvo una puntuacion de {puntuacion}  y fue filmada en {nacionalidad}
    2. Retornar si el año de la pelicula es mayor o igual o menor al pasado por parametro
    3. Cambiar el genero de una pelicula
    4. Modificar puntuacion de la pelicula (entre 1 y 10)
'''
class Peliculas:
    def __init__(self,nombre,anio,genero,nacionalidad,puntuacion):
        self.nombre = nombre
        self.anio = anio
        self.genero = genero
        self.nacionalidad = nacionalidad
        self.puntuacion = puntuacion
    
    def presentar_pelicula(self):
        print(f'La pelicula {self.nombre} de {self.genero} del {self.anio} obtuvo una puntuacion de {self.puntuacion}  y fue filmada en {self.nacionalidad}')
    
    def ver_anio(self,anio_comparar):
        if(self.anio<anio_comparar):
            print('La pelicula es mas vieja')
        elif(self.anio == anio_comparar):
            print('las peliculas son del mismo anio')
        else:
            print('La pelicula es mas nueva')
    
    def cambiar_genero(self,nuevo_genero):
        self.genero = nuevo_genero
    
    def cambiar_puntuacion(self,nueva_puntuacion):
        self.puntuacion = nueva_puntuacion