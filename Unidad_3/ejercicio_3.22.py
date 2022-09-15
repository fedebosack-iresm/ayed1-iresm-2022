"""
###**Ejercicio 3.22**
El programa debe:
*    Pedir al usuario cantidad de personas
*    pedir al usuario una a una la edad de las personas
*    Finalizado la carga de las edades debe imprimir por pantalla la edad mayor
*    No deben generar errores
"""
while True:
    try:
        cant_personas = int(input("Ingrese la cant de personas: "))
        if(cant_personas>0):
            break
        else:
            print('Ingresaste una cantidad negativa!!!')
    except:
        print('Error en la cant de personas')


for i in range(cant_personas):
    while True:
        try:
            edad = int(input(f"Ingrese la edad de la {i+1}° persona: "))
            if(i==0):
                edad_mayor = edad
                edad_menor = edad
            if(edad<0):
                print("La edad no puede ser negativa")
                continue
            if(edad > edad_mayor):
                edad_mayor = edad
            if(edad < edad_menor):
                edad_menor = edad
            break
        except:
            print("Error")

print(f"La mayor edad es: {edad_mayor}")
print(f"La menor edad es: {edad_menor}")
