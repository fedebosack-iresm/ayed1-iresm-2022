'''###**Ejercicio 2.4:**
El programa debe:
*  pedir por teclado el dinero actual de una persona
*  pedir por teclado el precio del insumo que quiere comprar en USD
*  convertir ese dinero a dolares( 1USD -> 280$)
*  devoler por pantalla True en caso que pueda comprar, False en caso que no
*  No deben aparecer errores'''
precio_dolar = 280
try:
    dinero_actual = float(input('Ingrese su dinero actual (ARS$): '))
    precio_insumo = float(input('Ingrese el precio del insumo ($USD): '))
    dinero_actual_usd = round((dinero_actual/precio_dolar),2)
    print(dinero_actual_usd)
    if(dinero_actual_usd >= precio_insumo):
        print('Puedo comprar el insumo')
except:
    print('Error! No escribiste numeros!')