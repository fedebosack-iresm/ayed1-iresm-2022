"""
###**Ejercicio 4.2 (Mediciones)**
El programa debe:
*   Contar con 4 funciones (calcular Area (cuadrado), calcular Perimetro(cuadrado),calcular Area (circulo), calcular Perimetro(circulo))
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los dos parametros y devolver el resultado al usuario
*   Gestionar posibles errores
"""
import funciones_geo as fg

menu = """
------Menu-----
1. Calcular Area (cuadrado)
2. Calcular Perimetro (cuadrado)
3. Calcular Area (circulo)
4. Calcular Perimetro (circulo)
5. Salir
Inrese una opcion: """
while True:
    
    opcion = input(menu)
    if(opcion == "1"):
        lado = fg.pedir_lado_cuadrado()
        print(f"El area del cuadrado es {fg.get_area(lado)} m2")
    elif(opcion == "2"):
        lado = fg.pedir_lado_cuadrado()
        print(f"El perimetro del cuadrado es {fg.get_perimetro(lado)} m")
    elif(opcion == "3"):
        radio = fg.pedir_radio_circulo()
        print(f"El area del circulo es {fg.get_area_circulo(radio)} m2")
    elif(opcion == "4"):
        radio = fg.pedir_radio_circulo()
        print(f"El perimetro del circulo es {fg.get_perimetro_circulo(radio)} m")
    elif(opcion == "5"):
        break
    else:
        print("opcion incorrecta")