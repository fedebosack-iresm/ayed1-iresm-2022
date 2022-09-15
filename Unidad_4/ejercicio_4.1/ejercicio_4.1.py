"""
###**Ejercicio 4.1 (Calculadora)**
El programa debe:
*   Contar con 4 funciones (suma, resta, división y multiplicación)
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los dos numero para operar y devolver el resultado al usuario
*   Gestionar posibles errores
"""
import funciones_math as fm

menu = """
------Menu-----
1. Suma
2. Resta
3. Multiplicacion
4. Dividir
5. Salir
Inrese una opcion: """
while True:
    num_1,num_2 = fm.pedir_numeros()
    opcion = input(menu)
    if(opcion == "1"):
        print(f"La suma de {num_1} y {num_2} es: {fm.suma(num_1,num_2)}")
    elif(opcion == "2"):
        print(f"La Resta de {num_1} y {num_2} es: {fm.resta(num_1,num_2)}")
    elif(opcion == "3"):
        print(f"La Multiplicacion de {num_1} y {num_2} es: {fm.multiplicacion(num_1,num_2)}")
    elif(opcion == "4"):
        print(f"La Division de {num_1} y {num_2} es: {fm.division(num_1,num_2)}")
    elif(opcion == "5"):
        break
    else:
        print("opcion incorrecta")