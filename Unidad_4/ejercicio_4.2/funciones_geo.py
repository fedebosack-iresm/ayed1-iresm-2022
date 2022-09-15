import math

def pedir_lado_cuadrado():
    while True:
        try:
            lado = float(input("Ingrese la medida del lado el cuadrado: "))
            if(lado > 0):
                return lado
            else:
                print("Error numero negativo!!")
        except:
            print("error en algun numero!!")

def pedir_radio_circulo():
    while True:
        try:
            radio = float(input("Ingrese la medida del radio del cirulo: "))
            if(radio > 0):
                return radio
            else:
                print("Error numero negativo!!")
        except:
            print("error en algun numero!!")

def get_area(lado):
    return lado*lado

def get_perimetro(lado):
    return 4*lado

def get_area_circulo(radio):
    return math.pi*math.pow(radio,2)

def get_perimetro_circulo(radio):
    return math.pi*radio*2