
def pedir_cantidad_tramos():
    while True:
        try:
            tramos = int(input('Ingrese la cantidad tramos del viaje: '))
            if(tramos > 0 and tramos <= 20):
                break
            else:
                print('El numero debe ser mayor a cero y menor o igual que 20')
        except:
            print('Error! debe ingresar un numero!!')
    
    return tramos

def calcular_suma(tramos):
    lista_tramos = [] # lista vacia
    for i in range(tramos):
        while True:
            try:
                tiempo_tramo = int(input(f'Ingrese el tiempo del {i+1}° tramo: '))
                if(tiempo_tramo > 0):
                    lista_tramos.append(tiempo_tramo)
                    break
                else:
                    print('El tramo no puede ser negativo!')
            except:
                print('Error! debe ingresar un numero!!')
    
    print(f'La suma de los tramos es: {int(sum(lista_tramos)/60)}:{sum(lista_tramos)%60} hh:mm')