'''
##**Ejercicio 5.11 (Empresa de Taxis)**
El programa debe:
*   Simular una empresa de taxis que cuente con tres Autos con sus respectivos cheferes
```
base_taxis =[["auto_1","auto_2","auto_3"],["chofer_1","chofer_2","chofer_3"],[45,50,30]]
```
*  Cada auto cuenta con un chofer y no hace recorridos mayores a lo q se le indica
*  Contar con 6 funciones disponibles en el menu:
    1. Preguntar al usuario el recorrido del viaje e indicar posibles autos y choferes
    2. Modificar nombre chofer segun el nombre del auto.
        auto_1 -> "federico"
    3. Modificar el recorrido segun el nombre del auto.
        auto_1 -> 60
    4. Agregar nuevo auto a la empresa de Taxis, indicando auto, nombre chofer y recorrido maximo -> ULTIMO
    5. imprimir la base con el siguiente formato
    6. Observar informacion de un chofer, verificando su existencia previamente

```
AUTO    -    CHOFER    -   RECORRIDO
auto_1  -   chofer_1   -      45
auto_2  -   chofer_2   -      50
auto_3  -   chofer_3   -      30
```
    
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''
# base taxis global
base_taxis =[["auto_1","auto_2","auto_3"],["chofer_1","chofer_2","chofer_3"],[45,50,30]]

def mostrar_base():
    print(f'-----------Base Taxis-----------')
    print(f'AUTO\tCHOFER\tRECORRIDO')
    for i in range(len(base_taxis[0])):
        print(f'{base_taxis[0][i]}\t{base_taxis[1][i]}\t{base_taxis[2][i]}')

def recorrido_autos():
    mostrar_base()
    while True:
        try:
            recorrido = float(input('Ingrese el recorrido: '))
            print(f'---------Autos con recorrido>{recorrido}---------')
            print(f'AUTO\tCHOFER\tRECORRIDO')
            for i in range(len(base_taxis[2])):
                if(base_taxis[2][i]>=recorrido):
                    print(f'{base_taxis[0][i]}\t{base_taxis[1][i]}\t{base_taxis[2][i]}')
            break

        except:
            print('Error, valor no numerico')

def modificar_nombre_chofer():
    global base_taxis
    mostrar_base()
    while True:
        auto = input('De que auto quiere modificar el chofer: ')
        if(auto in base_taxis[0]):
            indice = base_taxis[0].index(auto)
            nuevo_nombre = input('Ingrese el nuevo chofer: ')
            base_taxis[1][indice] = nuevo_nombre
            break
        else:
            print('No existe ese auto')

def agregar_auto():
    global base_taxis
    nuevo_auto = input('Ingrese el nuevo nombre del auto: ')
    chofer = input('Ingrese el nuevo nombre del chofer: ')
    while True:
        try:
            recorrido = int(input('Ingrese el nuevo recorrido: '))
            break
        except:
            print('Debe ser un numero')

    base_taxis[0].append(nuevo_auto)
    base_taxis[1].append(chofer)
    base_taxis[2].append(recorrido)

def eliminar_fila():
    global base_taxis
    mostrar_base()
    while True:
        auto = input('Ingrese el nombre del auto a eliminar: ')
        if(auto in base_taxis[0]):
            indice_eliminar = base_taxis[0].index(auto)
            base_taxis[0].pop(indice_eliminar)
            base_taxis[1].pop(indice_eliminar)
            base_taxis[2].pop(indice_eliminar)
            break
        else:
            print('No existe ese auto')




def menu():
    while True:
        menu = """
1. Preguntar al usuario el recorrido del viaje e indicar posibles autos y choferes
2. Modificar nombre chofer segun el nombre del auto.
3. Modificar el recorrido segun el nombre del auto.
4. Agregar nuevo auto a la empresa de Taxis, indicando auto, nombre chofer y recorrido maximo
5. imprimir la base con el siguiente formato
6. Observar informacion de un chofer, verificando su existencia previamente
7. Salir
8. Eliminar
Ingrese una opcion: """
        opcion = input(menu)
        if(opcion == '1'):
            recorrido_autos()
        elif(opcion == "2"):
            modificar_nombre_chofer()
        elif(opcion == "3"):
            pass #TAREA
        elif(opcion == "4"):
            agregar_auto()
        elif(opcion == "5"):
            mostrar_base()
        elif(opcion == "6"):
            pass #TAREA 
        elif(opcion == "7"):
           exit()
        elif(opcion == "8"):
           eliminar_fila() 
        else:
            print('Opcion incorrecta')