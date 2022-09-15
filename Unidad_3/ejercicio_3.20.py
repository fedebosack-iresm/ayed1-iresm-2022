"""
###**Ejercicio 3.20**
El programa debe:
*    Pedir al usuario una cantidad de tramos de un viaje
*    pedir al usuario la duracion en minutos de cada tramo
*    calcular el tiempo total de viaje
*    no deben generar errores
"""
while True:
    try:
        cant_tramos = int(input("Ingrese la cant de tramos: "))
        if(cant_tramos>0):
            break
        else:
            print('Ingresaste una cantidad negativa!!!')
    except:
        print('Error en la cant de tramos')

tiempo_total = 0
for i in range(cant_tramos):
    while True:
        try:
            tramo = float(input(f'Ingrese la duración del tramo {i+1}:'))
            tiempo_total+=tramo
            break
        except:
            print('No ingreso un numero')
print(f'Tiempo total = {tiempo_total}')