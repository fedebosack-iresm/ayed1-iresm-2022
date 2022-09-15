def ContarLetras(letra, palabra):
    letrasRepetidas = 0
    letra = letra.casefold()
    if(len(letra) != 1):
        return "Error con la letra"
    
    if(palabra == ""):
        return "La palabra no es valida"

    for i in palabra.casefold():
        if(i == " "):
            return "No valido frases" 
        if(i == letra):
            letrasRepetidas += 1

    return letrasRepetidas

def comparar_palabras(palabra_1,palabra_2):
    if(len(palabra_1) > len(palabra_2)):
        return palabra_1
    elif(len(palabra_1) < len(palabra_2)):
        return palabra_2
    else:
        return "mismo tamaño"