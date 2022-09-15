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