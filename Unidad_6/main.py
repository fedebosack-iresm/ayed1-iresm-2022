class Categoria:
    def __init__(self,nombre,tipo,peliculas):
        self.nombre = nombre
        self.tipo = tipo
        self.peliculas = peliculas

deportes = Categoria('deportes','deportes',['Los supercampeones','Space jam'])

print(deportes.peliculas)
