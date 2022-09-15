'''
### **Ejercicio 3.7:**
El programa debe:
*   Mostrar al usuario un menu
*   Permitir al usuario ingresar una opcion del menu
*   imprimir esa opcion
*   en caso de no escribir ninuna opcion del menu indicar ERROR

Condiciones:

1.   imprimir (string)
2.   1 (int)
3.   2 (int)
4.   salir (string)

Ayuda (como se comparan string y enteros **cuidado** con castear antes de verificar si el usuario ingreso str o int)
'''
menu = '''
--------MENU--------
1.   imprimir (string)
2.   sumar (int)
3.   restar (int)
4.   salir (string)
'''
print(menu)
opcion = input("Ingrese una opcion del menu: ")

if(opcion=="1"):
    print("Elegiste imprmir")
elif(opcion=="2"):
    print("Elegiste sumar")
elif(opcion=="3"):
    print("Elegiste restar")
elif(opcion=="4"):
    print("Elegiste salir")
else:
    print("No ingresaste ninguna opcion valida")