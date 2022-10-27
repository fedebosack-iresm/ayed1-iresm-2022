'''Ejercicio 5.2
Crear una funcion que debe:

Pedir al usuario una palabra o una frase
Indicar si esta se trata de un palindromo (ej: reconocer, neuquen, amor a roma)
No deben aparecer y se deben tener en cuenta todos los posibles errores'''

def reconocer_palindromo():
    ingreso = input('Ingrese una palabra o frase: ')
    lista_string = list(ingreso)
    lista_reversa = lista_string.copy()
    lista_reversa.reverse()
    if(lista_string==lista_reversa):
        print(f'{ingreso} es palindromo')
    else:
        print(f'{ingreso} NO es palindromo')

reconocer_palindromo()