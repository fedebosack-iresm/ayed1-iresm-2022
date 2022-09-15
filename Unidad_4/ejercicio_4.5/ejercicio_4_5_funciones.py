#variables globales
usuario_defecto = 'user' 
contrasena_defecto = '1234'
saldo = 50000

def consultar_saldo():
    global saldo #saldo global
    print(f'Su saldo es: {saldo}')

def ingreso_user_contra():
    for i in range(3):
        user = input('Ingrese el usuario: ')
        contra = input('Ingrese la contraseña: ')
        if(user == usuario_defecto and contra == contrasena_defecto):
            print('Ingreso correcto!')
            return True
        else:
            print(f'Error, te quedan {2-i} intentos')
            
    return False

def ingreso_dinero():
    while True:
        try:
            global saldo #saldo global
            dinero = float(input("Ingrese su dinero: "))
            saldo = saldo + dinero
            consultar_saldo()#es lo mismo que el print
            #print(f'Su saldo es: {saldo}')
            return
        except:
            print("Error!")

def retirar_dinero():
    global saldo #saldo global
    dinero = float(input("Ingrese su dinero a retirar: "))
    if(retirar_dinero<=saldo):
        saldo = saldo - dinero
        consultar_saldo()
        #print(f'Su saldo es: {saldo}')
        return
    else:
        print("Error! Su saldo es insuficiente ")
        
def menu(flag):
    while flag:
        menu = """
        1.  Consultar el saldo
        2.  Ingresar dinero y actualizar saldo
        3.  Retirar dinero y actualizar saldo
        4.  Salir y volver al menu
        5.  Cerrar
        Ingrese una opcion: """
        opcion = input(menu)
        if(opcion == '1'):
            consultar_saldo()
        elif(opcion == '2'):
            ingreso_dinero()
        elif(opcion == '3'):
            retirar_dinero()
        elif(opcion == '4'):
            print("usted a salido, lo esperamos, la propina de jaky es de axel")
            break
        elif(opcion == "5"):
           print("Nos vemos en Disney")
           exit()
        else:
            print('Opcion incorrecta')
    
        