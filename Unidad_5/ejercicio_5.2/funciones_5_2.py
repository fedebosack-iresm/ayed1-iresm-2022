
def pedir_cantidad():
    while True:
        try:
            cant_personas = int(input('Ingrese la cantidad de personas a ingresas su edad: '))
            if(cant_personas > 0 and cant_personas <= 20):
                break
            else:
                print('El numero debe ser mayor a cero y menor o igual que 20')
        except:
            print('Error! debe ingresar un numero!!')
    
    return cant_personas

def cargar_edades(cant_personas):
    lista_edades = [] # lista vacia
    for i in range(cant_personas):
        while True:
            try:
                edad_persona = int(input(f'Ingrese la edad de la {i+1}° persona: '))
                if(edad_persona > 0 and edad_persona <100):
                    lista_edades.append(edad_persona)
                    break
                else:
                    print('La persona no puede tener edad negativa!')
            except:
                print('Error! debe ingresar un numero!!')
    
    lista_edades.sort()
    print(f'La mayor edad es {lista_edades[-1]}')