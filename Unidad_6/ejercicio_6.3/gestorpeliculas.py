'''El programa debe:
*   Tener un menu con 4 opciones: (GestorPeliculas)
    1. Crear una pelicula y guardar su nombre en una lista de peliculas.
    2. Verificar si la pelicula deseada existe en la lista de peliculas.
    3. Pedir a la lista de peliculas, todas las de un año.
    4. Presentar una pelicula de la lista
    5. Cambiar el genero de una pelicula'''
import peliculas as pe

class GestorPeliculas:
    def __init__(self):
        self.lista_peliculas = []
        
    def crear_pelicula(self):
        nombre = input('Ingrese el nombre de la pelicula: ')
        while True:
            try:
                anio = int(input('Ingrese el año de la pelicula: '))
                break
            except:
                print('error')
        genero = input('Ingrese el genero de la pelicula: ')
        nacionalidad = input('Ingrese la nacionalidad de la pelicula: ')
        while True:
            try:
                puntuacion = int(input('Ingrese la puntuacion de la pelicula: '))
                break
            except:
                print('error')
        pelicula = pe.Peliculas(nombre,anio,genero,nacionalidad,puntuacion)
        self.lista_peliculas.append(pelicula)
    
    def presentar_peliculas(self):
        for pel in self.lista_peliculas:
            pel.presentar_pelicula()
    
    def verificar_peliculas_anio(self,anio_verificar):
        for pel in self.lista_peliculas:
            if(pel.anio == anio_verificar):
                pel.presentar_pelicula()
    
    def verificar_pelicula(self,pelicula_verificar):
        for pel in self.lista_peliculas:
            if(pel.nombre == pelicula_verificar):
                print('La pelicula existe')
                return
            
        print('La pelicula No existe')
    
    def cambiar_genero(self,nombre,nuevo_genero):
        for pel in self.lista_peliculas:
            if(pel.nombre == nombre):
                pel.genero = nuevo_genero
                print('Genero cambiado')
            
        
            