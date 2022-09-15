# Variables globales de los productos
prod_1_cod = 1
prod_2_cod = 2
prod_3_cod = 3

prod_1_nom = 'producto1'
prod_2_nom = 'producto2'
prod_3_nom = 'producto3'

prod_1_pre = 300
prod_2_pre = 400
prod_3_pre = 500

prod_1_sto = 5
prod_2_sto = 4
prod_3_sto = 7

def agregar_stock():
    menu_productos()
    while True:
        cod = input('Indique el producto que desea agregar stock: ')
        if(cod == '1' or cod == '2' or cod == '3'):
            while True:
                try:
                    stock = int(input("Ingrese el stock a agregar: "))
                    if(stock<=0):
                        print('El stock no puede ser menor o igual a cero')
                    else:
                        break
                except:
                    print("Error!")
            
            if(cod =='1'):
                global prod_1_sto
                prod_1_sto+=stock
            elif(cod =='2'):
                global prod_2_sto
                prod_2_sto+=stock
            elif(cod =='3'):
                global prod_3_sto
                prod_3_sto+=stock

            menu_productos()
            return
        else:
            print('Opcion incorrecta')

def cambiar_precio():
    menu_productos()
    while True:
        cod = input('Indique el producto que desea cambiar el precio: ')
        if(cod == '1' or cod == '2' or cod == '3'):
            while True:
                try:
                    precio = int(input("Ingrese nuevo precio: "))
                    if(precio<=0):
                        print('El precio no puede ser menor o igual a cero')
                    else:
                        break
                except:
                    print("Error!")
            
            if(cod =='1'):
                global prod_1_pre
                prod_1_pre = precio
            elif(cod =='2'):
                global prod_2_pre
                prod_2_pre = precio
            elif(cod =='3'):
                global prod_3_pre
                prod_3_pre = precio

            menu_productos()
            return
        else:
            print('Opcion incorrecta')

def menu_productos():
    print(f'-----------Menu-----------')
    print(f'Codigo\tNombre\t\tPrecio\tStock')
    print(f'{prod_1_cod}\t{prod_1_nom}\t{prod_1_pre}\t{prod_1_sto}')
    print(f'{prod_2_cod}\t{prod_2_nom}\t{prod_2_pre}\t{prod_2_sto}')
    print(f'{prod_3_cod}\t{prod_3_nom}\t{prod_3_pre}\t{prod_3_sto}')

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
            pass
        elif(opcion == '3'):
            pass
        elif(opcion == '4'):
            pass
        elif(opcion == "5"):
           pass
        elif(opcion == "6"):
           agregar_stock()
        elif(opcion == "7"):
           cambiar_precio()
        elif(opcion == "8"):
           exit()
        else:
            print('Opcion incorrecta')