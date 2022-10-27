"""
##**Ejercicio 4.10 (Programa de ventas) con listas dentro de listas**
El programa debe:
*   Simular un programa que venda 3 productos

Codigo   Nombre    Precio  Stock
1   &   producto1   & 300  & 5
2   &   producto2   & 400  & 4
3   &   producto3   & 500  & 7

*   El menu debe mostrar los productos a comprar.
*   Luego se debe contar con un menu de si se pagara en efectivo o tarjeta credito o debito
*   Contar con 7 funciones:
  1.  Ver menu de productos
  2.  Pagar con tarjeta credito (Se debe cobrar 10% mas y se debe descontar el stock)
  3.  Pagar con tarjeta debito (se debe descontar el stock)
  4.  Pagar con efectivo (Se debe cobrar 10% menos y se debe descontar el stock)
  5.  consultar productos y stock
  6.  agregar stock a los productos
  7.  cambiar el precio a los productos
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
"""

# variable global lista
from email.mime import base


base_productos = [['1','2','3'],['producto1','producto2','producto3'],[300,400,500],[5,4,7]]

def menu_productos():
    print(f'-----------Menu-----------')
    print(f'Codigo\tNombre\t\tPrecio\tStock')
    for i in range(len(base_productos[0])):
        print(f'{base_productos[0][i]}\t{base_productos[1][i]}\t{base_productos[2][i]}\t{base_productos[3][i]}')

def pagar_credito():
    global base_productos
    menu_productos()
    while True:
        opcion = input('Elija el producto a comprar con el codigo: ')
        if(opcion in base_productos[0]):
            indice = base_productos[0].index(opcion) #para obtener la fila del producto
            if(base_productos[3][indice]>0):
                print(f'Indice: {indice}')
                print(f'Usted debe pagar {base_productos[2][indice]*1.1}')
                base_productos[3][indice]-=1
                break
            else:
                print('No hay stock de ese producto')
        else:
            print('No existe el producto')

def pagar_debito():
    global base_productos
    menu_productos()
    while True:
        opcion = input('Elija el producto a comprar con el codigo: ')
        if(opcion in base_productos[0]):
            indice = base_productos[0].index(opcion) #para obtener la fila del producto
            if(base_productos[3][indice]>0):
                print(f'Indice: {indice}')
                print(f'Usted debe pagar {base_productos[2][indice]}')
                base_productos[3][indice]-=1
                break
            else:
                print('No hay stock de ese producto')
        else:
            print('No existe el producto')

def pagar_efectivo():
    global base_productos
    menu_productos()
    while True:
        opcion = input('Elija el producto a comprar con el codigo: ')
        if(opcion in base_productos[0]):
            indice = base_productos[0].index(opcion) #para obtener la fila del producto
            if(base_productos[3][indice]>0):
                print(f'Indice: {indice}')
                print(f'Usted debe pagar {base_productos[2][indice]*0.9}')
                base_productos[3][indice]-=1
                break
            else:
                print('No hay stock de ese producto')
        else:
            print('No existe el producto')

def mostrar_prod_stock():
    print(f'-----------Menu-----------')
    print(f'\tNombre\tStock')
    for i in range(len(base_productos[0])):
        print(f'{base_productos[1][i]}\t{base_productos[4][i]}')

def agregar_stock():
    global base_productos
    menu_productos()
    while True:
        opcion = input('Elija el producto a agregar stock con el codigo: ')
        if(opcion in base_productos[0]):
            indice = base_productos[0].index(opcion) #para obtener la fila del producto
            while True:
                try:
                    cant_agregar = int(input('Ingrese la cant a agregar: '))
                    if(cant_agregar>0):
                        base_productos[2][indice]+=cant_agregar
                        return
                    else:
                        print('La cant debe ser mayor a cero')
                    
                except:
                    print('El valor debe ser numerico')
        else:
            print('No existe el producto')

def cambiar_precio():
    global base_productos
    menu_productos()
    while True:
        opcion = input('Elija el producto a cambiar el precio (con el codigo): ')
        if(opcion in base_productos[0]):
            indice = base_productos[0].index(opcion) #para obtener la fila del producto
            while True:
                try:
                    nuevo_precio = int(input('Ingrese el nuevo precio: '))
                    if(nuevo_precio>=0):
                        base_productos[2][indice] = nuevo_precio
                        return
                    else:
                        print('La cant debe ser mayor a cero')
                    
                except:
                    print('El valor debe ser numerico')
        else:
            print('No existe el producto')

def menu():
    while True:
        menu = """
1.  Ver menu de productos
2.  Pagar con tarjeta credito (Se debe cobrar 10% mas y se debe descontar el stock)
3.  Pagar con tarjeta debito (se debe descontar el stock)
4.  Pagar con efectivo (Se debe cobrar 10% menos y se debe descontar el stock)
5.  Consultar productos y stock
6.  Agregar stock a los productos
7.  Cambiar el precio a los productos
8.  Salir
Ingrese una opcion: """
        opcion = input(menu)
        if(opcion == '1'):
            menu_productos()
        elif(opcion == '2'):
            pagar_credito()
        elif(opcion == '3'):
            pagar_debito()
        elif(opcion == '4'):
            pagar_efectivo()
        elif(opcion == "5"):
           mostrar_prod_stock()
        elif(opcion == "6"):
           agregar_stock()
        elif(opcion == "7"):
           cambiar_precio()
        elif(opcion == "8"):
           exit()
        else:
            print('Opcion incorrecta')