def funcion_2(lista_abc):
    # lista_abc iteramos
    # lista_aux vacia
    lista_aux = []

    for i in range(len(lista_abc)):
        letra = lista_abc[i]
        if(letra == 'a' or letra == 'e' or letra == 'i'or letra == 'o' or letra == 'u'):
            lista_aux.append(letra)
    print(lista_aux)

abc = "abcdefghijklmnñopqrstuvwxyz"
lista_abc = list(abc)
print(lista_abc)
funcion_2(lista_abc)

