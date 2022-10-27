class Persona:
    # constructor
    def __init__(self,nombre,apellido,edad,ciudad_de_recidencia):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad_de_recidencia = ciudad_de_recidencia

    def presentarse(self):
        print(f'Soy {self.nombre} {self.apellido}, tengo {self.edad} años y vivo en {self.ciudad_de_recidencia}')

    def get_edad(self):
        if(self.edad < 14 and self.edad > 0):
            print('Soy un niño')
        elif(self.edad >= 14 and self.edad < 22):
            print('Soy un Adolecente')
        elif(self.edad >= 22 and self.edad < 30):
            print('Soy un Joven')
        elif(self.edad >= 30 and self.edad < 50):
            print('Soy un Adulto')
        elif(self.edad >= 50 and self.edad < 120):
            print('Soy muy Adulto')
