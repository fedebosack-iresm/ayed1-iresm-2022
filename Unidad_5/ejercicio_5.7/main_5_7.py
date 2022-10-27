'''##**Ejercicio 5.7 (Programa de Inventario de verduleria)**
Crear un prgrama que debe:
*    Contar con un stock de frutas y otro de verduras
    (El stock indica si venden o no esa fruta o verdura, no la cantidad)
    - dos listas que inician vacias
*    Contar con un menu y 3 funciones

      1. Agregar frutas o verduras al correspondiente stock (verificando que que sean nuevas)
      2. Consultar el stock de frutas o verduras
      3. Eliminar un elemento del stock'''

lista_frutas = []

def agregar_fruta():
    global lista_frutas
    fruta = input('Ingrese fruta: ')
    if(fruta not in lista_frutas):
        lista_frutas.append(fruta)

def menu(flag):
    while flag:
        menu = """
        1.  Agregar frutas
        2.  Agregar verdura
        3.  Consultar el stock de frutas
        4.  Consultar el stock de verdura
        5.  Eliminar fruta
        6.  Eliminar verdura
        7.  Salir
        Ingrese una opcion: """
        opcion = input(menu)
        if(opcion == '1'):
            agregar_fruta()
        elif(opcion == '2'):
            pass
        elif(opcion == '3'):
            print(lista_frutas)
        elif(opcion == '4'):
            pass
        elif(opcion == "5"):
           pass
        elif(opcion == '6'):
            pass
        elif(opcion == "7"):
           exit()
        else:
            print('Opcion incorrecta')

menu(True)