"""
###**Ejercicio 4.3 (Palabras)**
El programa debe:
*   Contar con 3 funciones:
  1. Contador de letras (letra,palabra): Debe contar la cantidad de letras que tiene una palabra o frase (Ambos parametros)
  2. Comparador de palabras (palabra1 vs palabra2): debe comparar que palabra tiene mas letras. 
     IMPORANTE: deben ser palabras y no frases (verificar)
  3. Quitador de vocales(palabra a retirar las vocales): debe recibir una palabra o frase y quitar todas las vocales
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los parametros y devolver el resultado al usuario
*   Gestionar posibles errores
"""
import funciones_palabras as fp
menu = """
------Menu-----
1. Contar letras
2. Comparar palabras
3. Quitar vocales
4. Salir
Inrese una opcion: """
while True:
    
    opcion = input(menu)
    if(opcion == "1"):
        letra = input("ingrese una letra: ")
        palabra = input("Ingrese una palabra: ")
        cant_letras = fp.ContarLetras(letra,palabra)
        print(f"{palabra} tiene {cant_letras} {letra}")
    elif(opcion == "2"):
        palabra_1 = input("Ingrese una palabra: ")
        palabra_2 = input("Ingrese otra palabra: ")
        print(f"La palabra de mayor tamaño es:{fp.comparar_palabras(palabra_1,palabra_2)}")
    elif(opcion == "3"):
        pass
    elif(opcion == "4"):
        break
    else:
        print("opcion incorrecta")