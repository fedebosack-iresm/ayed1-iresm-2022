'''
####**Ejercicio 3.2**
*Agencia de autos:*

El programa cuenta con tres marcas de autos y su precio.

El programa debe:
*   pedir al usuario que ingrese la cant de dinero que dispone.
*   verificar que la cantidad ingresada sea un numero y sino mostrar error
*   verificar la cantidad de ingresada e indicar que auto o autos puede comprar
'''
#precios de los autos
p_auto_ford = 10000
p_auto_renault = 50000
p_auto_tesla = 600000
dinero = -1
try:
    dinero = float(input('Ingrese su dinero disponible: '))
except:
    print('Error!, no ingresaste un valor numerico')

if(dinero >= p_auto_renault):
    print('Puede comprar un ford y un renault')
elif(dinero >= p_auto_renault):
    print('Puede comprar un renault')
elif(dinero >= p_auto_tesla):
    print('Puede comprar un tesla')
else:
    print('No podes comprar ningun auto')
