'''
##**Ejercicio 5.6**
Crear una funcion que debe:
*   Tener almacenado el abcedario en una lista
*   Pedir al usuario un numero (2 o 3) - VERIFICAR que el num ingresado sea 2 o 3
*   Elimina de la lista las letras que ocupen posiciones múltiplos de ese numero
*   Mostrar por pantalla la lista resultante.
*   No deben aparecer y se deben tener en cuenta todos los posibles errores'''

def funcion_1(lista_abc):
    # lista_abc iteramos
    # lista_aux eliminamos valores
    lista_aux = lista_abc.copy()

    for i in range(len(lista_abc)):
        if((i+1)%num == 0):
            elemento = lista_abc[i]
            lista_aux.remove(elemento)
    print(lista_aux)

def funcion_2(lista_abc):
    # lista_abc iteramos
    # lista_aux vacia
    lista_aux = []

    for i in range(len(lista_abc)):
        if((i+1)%num != 0):
            elemento = lista_abc[i]
            lista_aux.append(elemento)
    print(lista_aux)

abc = "abcdefghijklmnñopqrstuvwxyz"
lista_abc = list(abc)

while True:
    try:
        num = int(input('Ingrese un 2 o 3: '))
        if(num==2 or num==3):
            break
        else:
            print('Debe ingresar un 2 o 3!!')
    except:
        print('No ingreso un numero')
print(lista_abc)

funcion_1(lista_abc)
funcion_2(lista_abc)
