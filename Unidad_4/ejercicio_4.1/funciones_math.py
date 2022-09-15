def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    try:
        return a/b
    except:
        return "ERROR"

def pedir_numeros():
    while True:
        try:
            num_1 = float(input("Ingrese el 1° num: "))
            num_2 = float(input("Ingrese el 2° num: "))
            break
        except:
            print("error en algun numero!!")
    return num_1,num_2