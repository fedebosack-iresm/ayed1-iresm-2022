'''
### **Ejercicio 3.5**
El programa debe :
*   Almacenar una variable `contraseña` con una contraseña
*   Preguntar al usuario por la contraseña e imprimir por pantalla si la contraseña introducida por el usuario coincide o no con la variable
 **IMPORTANTE**: sin tener en cuenta mayúsculas y minúsculas.(metodos string)
*   no debe generar errores
'''
contraseña = "HOLA"
contraseña_usuario = input("Ingrese la contraseña: ")
if(contraseña.casefold() == contraseña_usuario.casefold()):
  print("contraeña correcta")
else:
  print("contraseña incorrecta")