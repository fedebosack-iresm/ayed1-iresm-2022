'''##**Ejercicio 2.6**
El programa debe:
- pedir en orden el Nombre, apellido, edad y numero de calzado
- verificar que cada uno sea el tipo de variable correcto (IMPORTANTE)
- en caso verdadero imprimir de la siguiente manera el resultado:
  ejemplo
  Nombre: Lionel
  Apellido: Messi
  Edad: 34
  Numero de Calzado: 42.5
- en caso contrario imprimir error'''

nombre = input("Ingrese el nombre: ").capitalize()
apellido = input("Ingrese el Apellido: ").capitalize()
try:
    edad = int(input("Ingrese la edad: "))
    calzado = float(input("Ingrese el calzado: "))
    print(f'- Nombre: {nombre}\n- Apellido: {apellido}\n- Edad: {edad}\n- Calzado: {calzado}')
except:
    print("ERROR! La edad o el calzado son incorrectos")
