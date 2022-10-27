class FiguraGeometrica:
    def __init__(self,tipo_de_figura,color,tamanio='pequeño'):
        self.tipo_de_figura = tipo_de_figura
        self.color = color
        self.tamanio = tamanio

    def presentarse(self):
        print(f'Un {self.tipo_de_figura} de color {self.color} y tamaño {self.tamanio}')
    
    def cambiar_color(self,nuevo_color):
        self.color = nuevo_color
        print(f'Nuevo color: {self.color}')

    def verificar_tamanio(self):
        if(self.tamanio == 'pequeño'):
            self.tamanio='grande'
            print('Se cambio a grande')
        else:
            print('No era pequeño')