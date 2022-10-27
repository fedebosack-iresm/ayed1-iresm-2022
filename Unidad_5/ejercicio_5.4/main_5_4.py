'''##**Ejercicio 5.4**
Crear funciones que deban:

*    Pedir al usuario 5 materias (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
*    Verficiar que sea un nombre correcto
*    Almacenar los nombres en una lista
*    Mostrar las materias en orden alfabetico
*    No deben aparecer y se deben tener en cuenta todos los posibles errores'''

def pedir_mat():
    lista_materias = []
    for i in range(5):
        while True:
            materia = input(f'Pone la materia {i+1} \n')
            if (materia.isalpha()):
                lista_materias.append(materia)
                break
            else:
                print('Nombre incorrecto')
    
    lista_materias.sort()
    print(lista_materias)

pedir_mat()