'''
##**Ejercicio 5.15 (Base de peliculas)**
El programa debe:
*   Simular una base de datos de peliculas y series con la capacidad de agregar, buscar, eliminar y filtrar peliculas y series.
*   Debe comenzar con las siguientes peliculas y series en un diccionario:

```
base = {
    "peliculas" : ["El hombre araña", "Los vengadores" , "Los vengadores 2"],
    "series" : ["prision break", "la casa de papel" , "los simpsons"]
        }
```

*   Contar con 5 funciones disponibles en el menu:
    1. Mostrar por pantalla en formato vertical la lista de peliculas o series disponibles.
    2. Agregar nuevas peliculas o series (que no esten) en la base.
    3. Eliminar peliculas o series de la base.
    4. Mostrar segun requiera el usuario la lista de peliculas desde un punto a otro (ej el usuario quiere ver de la 2° a la 4° una lista ).
    5. Buscar peliculas o series que contengan una palabra requerida por el usuario. (ej. input("el"), se liste las peliculas que contengan la palabra "el").
'''
base = {
    "peliculas" : ["El hombre araña", "Los vengadores" , "Los vengadores 2"],
    "series" : ["prision break", "la casa de papel" , "los simpsons"]
        }

def listar_serie_pelicula():
    while True:
        lista = input('Que desea listar (series o peliculas): ')
        if(lista in base): # verifico que exista el key
            print(f'----Lista de {lista}----')
            lista_de_so_p = base[lista]
            for i in lista_de_so_p:
                print(i)
            break
        else:
            print('Clave incorrecta')

def agregar_serie_pelicula():
    while True:
        lista = input('Que desea agregar (series o peliculas): ')
        if(lista in base): # verifico que exista el key
            s_p_agregar = input('Ingrese el nombre de la serie o pelicula: ')
            lista_de_so_p = base[lista] #obtengo la lista de series o peliculas
            if(s_p_agregar not in lista_de_so_p):
                lista_de_so_p.append(s_p_agregar)
                break
            else:
                print('Esa serie o pelicula ya existe')
        else:
            print('Clave incorrecta')

def eliminar_serie_pelicula():
    while True:
        lista = input('Que desea eliminar (series o peliculas): ')
        if(lista in base): # verifico que exista el key
            s_p_agregar = input('Ingrese el nombre de la serie o pelicula a eliminar: ')
            lista_de_so_p = base[lista] #obtengo la lista de series o peliculas
            if(s_p_agregar in lista_de_so_p):
                lista_de_so_p.remove(s_p_agregar)
                break
            else:
                print('Esa serie o pelicula no existe')
        else:
            print('Clave incorrecta')

def ver_serie_pelicula():
    while True:
        lista = input('Que desea ver (series o peliculas): ')
        if(lista in base): # verifico que exista el key
            while True:
                try:
                    inicio = int(input('Ingrese el inicio de la lista: '))
                    fin = int(input('Ingrese el fin de la lista: '))
                    break
                except:
                    print('eror')
            print(f'----Lista de {lista}----')
            lista_de_so_p = base[lista]
            #lista_cortada = lista_de_so_p[inicio-1:fin]
            for i in range(inicio-1,fin):
                print(lista_de_so_p[i])
            break
        else:
            print('Clave incorrecta')

def buscar_serie_pelicula():
    while True:
        palabra_a_buscar = input('buscar: ')
        lista_peliculas = base['peliculas']
        lista_series = base['series']
        for pel in lista_peliculas:
            if(palabra_a_buscar.capitalize() in pel.capitalize()):
                print(pel)
        for ser in lista_series:
            if(palabra_a_buscar.capitalize() in ser.capitalize()):
                print(ser)



def menu():
    while True:
        menu = """
-----------------MENU-----------------
1. Mostrar por pantalla peliculas o series disponibles.
2. Agregar nuevas peliculas o series.
3. Eliminar peliculas o series de la base.
4. Mostrarla lista de peliculas o series desde un punto a otro
5. Buscar peliculas o series que contengan una palabra requerida por el usuario.
Ingrese una opcion: """
        opcion = input(menu)
        if(opcion == "1"):
            listar_serie_pelicula()
        elif(opcion == "2"):
            agregar_serie_pelicula()
        elif(opcion == "3"):
            eliminar_serie_pelicula()
        elif(opcion == "4"):
            ver_serie_pelicula()
        elif(opcion == "5"):
            pass
        elif(opcion == "6"):
            exit()
        else:
            print("Opcion incorrecta")

menu()