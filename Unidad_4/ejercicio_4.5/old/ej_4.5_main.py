"""
##**Ejercicio 4.5 (Cajero automatico)**
El programa debe:
*   Simular un cajero automatico y pedir usuario y contraseña (user, 1234) caso verdadero mostrar menu y en caso falso seguir pidiendo.
*   En caso de mal ingreso de usuario o contraseña 3 veces el programa debe detenerse
*   El menu debe mostrar las funciones posteriores.
*   Contar con 4 funciones:
  1.  Consultar el saldo (inicio de 50000)
  2.  Ingresar dinero y actualizar saldo
  3.  Retirar dinero y actualizar saldo
  4.  Salir, y volver al menu de usuario y contraseña
*   Gestionar posibles errores"""

import funciones_ej_4_5 as fu

flag = fu.ingreso_user_contra()

while flag:
    menu = """
1.  Consultar el saldo
2.  Ingresar dinero y actualizar saldo
3.  Retirar dinero y actualizar saldo
4.  Salir
Ingrese una opcion: """
    opcion = input(menu)
    if(opcion == '1'):
        fu.consultar_saldo()
    elif(opcion == '2'):
        pass
    elif(opcion == '3'):
        pass
    elif(opcion == '4'):
        break
    else:
        print('Opcion incorrecta')
    