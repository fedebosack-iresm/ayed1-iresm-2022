'''
************************************************************
 MATERIA: Algoritmos y Estructuras de Datos 1
 EXAMEN: Simulacro Examen 1
 APELLIDO Y NOMBRE: 
 DNI: 
 CARRERA: 
 AÑO: 2022 
 Se debe adjuntar archivos comprimidos en classroom con el siguiente nombre "[AYEDI 2022 - Apellido, Nombre - 1°Examen]" - No necesario
 ************************************************************
 Ítems a evaluar:
 1. Contenidos de la materia
 2. Requerimientos y comprensión de consignas
 3. Estructura (modularización), legibilidad y comentarios del código.

¡Cualquier duda con el enunciado consultar al docente!
************************************************************
ENUNCIADO: "Programa de Gestión Videojuegos"

Introduccion: 
    El siguiente programa consiste en un software de gestion de videojuegos.
    El programa debe permitir agregar y quitar videojuegos al sistema junto con su informacion: 
    Nombre, Año, Categoria.

Requerimientos:
El programa debe:
*   Contar con un menu donde permita al usuario elegir entre las siguientes funciones:
    1. Permitir al usuario del programa agregar un nuevo videojuego (Indicando: Nombre - Año - Categoria)
       Verificando: Que el nombre no exista previamente, el año este entre 1990 y 2021 y que la categoria corresponda
       con una lista de categorias.(Ayuda: metodo in de list)
       IMPORTANTE: se debe crear una matriz para contener los datos, listas dentro de listas.
    2. Ver lista de videojuegos (Formato: Nombre - Año - Categoria)
    3. Editar la categoria de un video juego verificando que exista la categoria, se edita mediante el nombre.
    4. Ver lista de categorias.
    5. Agregar categorias al sistema, poniendo automaticamente la primera letra mayuscula (verificando que no exista previamente).
    6. Eliminar una categoria del sistema, verificando previamente su existencia
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio (minimo un archivo main y otro de funciones)
'''
categorias = ["Accion", "Deportivo", "Estrategia", "Simulación"]
video_juegos = [[],[],[]]

def agregar_video_juego():
    global video_juegos
    while True:
        nombre = input('Ingrese el nombre del video juego: ')
        if(nombre not in video_juegos[0]):
            break
        else:
            print('El nombre ya existe')

    while True:
        try:
            anio = int(input('Ingrese el año del video juego: '))
            if(1990 <= anio <= 2021):
                break
            else:
                print('Valor de año incorrecto, debe estar entre 1990 y 2021')
        except:
            print('Debe ingresar un valor numerico')

    while True:
        categoria = input('Ingrese la categoria del video juego: ')
        if(categoria.capitalize() in categorias):
            break
        else:
            print('La categoria no existe')
    
    video_juegos[0].append(nombre)
    video_juegos[1].append(anio)
    video_juegos[2].append(categoria)

def mostrar_videojuegos():
    print(f'-----------Base Video Juegos-----------')
    print(f'Nombre\tAño\tCategoria')
    cant_filas = len(video_juegos[0])
    for i in range(cant_filas): #iteramos la cantidad de filas
        print(f'{video_juegos[0][i]}\t{video_juegos[1][i]}\t{video_juegos[2][i]}')

def editar_categoria():
    global video_juegos
    mostrar_videojuegos()
    while True:
        nombre = input('De que nombre quiere modificar la categoria: ')
        if(nombre in video_juegos[0]): #verificamos el nombre
            indice = video_juegos[0].index(nombre)
            # Estaria bueno ver la lista de categorias
            nuevo_categoria = input('Ingrese la nueva categoria: ')
            while True:
                categoria = input('Ingrese la categoria del video juego: ')
                if(categoria.capitalize() in categorias):
                    video_juegos[2][indice] = nuevo_categoria
                    break
                else:
                    print('La categoria no existe')
            break
        else:
            print('No existe ese nombre en la base')

def mostrar_categorias():
    print(f'-----------Base Categorias-----------')
    for i in categorias: #iteramos la cantidad de filas
        print(f'{i}')

def agregar_categorias():
    while True:
        categoria = input('Ingrese la nueva categoria: ')
        if(categoria.capitalize() not in categorias):
            video_juegos[2].append(categoria.capitalize())
            break
        else:
            print('La categoria no existe')

def eliminar_categorias():
    while True:
        categoria = input('Ingrese la categoria a eliminar: ')
        if(categoria.capitalize() in categorias):
            video_juegos[2].remove(categoria.capitalize())
            break
        else:
            print('La categoria no existe')
    
def menu():
    while True:
        menu = '''
1. Permitir al usuario del programa agregar un nuevo videojuego
2. Ver lista de videojuegos (Formato: Nombre - Año - Categoria)
3. Editar la categoria de un video juego verificando que exista la categoria, se edita mediante el nombre.
4. Ver lista de categorias.
5. Agregar categorias al sistema, poniendo automaticamente la primera letra mayuscula (verificando que no exista previamente).
6. Eliminar una categoria del sistema, verificando previamente su existencia
7. Salir
Indique la opcion: '''
        opcion = input(menu)
        if(opcion == '1'):
            agregar_video_juego()
        elif(opcion == "2"):
            mostrar_videojuegos()
        elif(opcion == "3"):
            editar_categoria() 
        elif(opcion == "4"):
            mostrar_categorias()
        elif(opcion == "5"):
            agregar_categorias()
        elif(opcion == "6"):
            eliminar_categorias() 
        elif(opcion == "7"):
           exit()
        else:
            print('Opcion incorrecta')