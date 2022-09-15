"""
###**Ejercicio 4.4 (Conversor de unidades)**
El programa debe:
*   Contar con 4 funciones:
  1.  Conversor de Grados Celcius a Fahrenheit(temperatura en °C).(buscar regla)
  2.  Conversor de cm3 a litros (cantidad de cm3)
  3.  Conversor de litros a cm3 (cantidad de litros)
  4.  Pesos a Dolares (pesos)
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los parametros y devolver el resultado al usuario
*   Gestionar posibles errores
"""
import funciones_conversion as fc
menu = """
------Menu-
1. Grados a Cº a F
2. cm3 a litros
3. litros a cm3
4. Pesos a dolares
5. Salir
Inrese una opcion: """
while True:
    opcion = input(menu)
    if (opcion == '1'):
        temp_ce = fc.pedir_temperatura()
        fc.trans_c_f(temp_ce)
    elif (opcion == '2'):
        cm = fc.pedir_cm()
        fc.trans_cm_a_l(cm)
    elif (opcion == '3'):
        li = fc.pedir_li()
        fc.trans_l_a_cm(li)
    elif (opcion == '4'):
        pesos = fc.pedir_pesos()
        fc.pesos_dolares(pesos)
    elif (opcion == '5'):
        break
    else:
        print("Invalid opcion")
