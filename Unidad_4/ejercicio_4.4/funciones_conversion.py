def pedir_temperatura():
    while True:
        try:
            temp = float(input('Ingrese la temperatura: '))
            return temp
        except:
            print('error')


def trans_c_f(temp):
    fa = temp*1.8+32.2
    print(f'{temp} ºC = {fa} ºF')


def pedir_cm():
    while True:
        try:
            cm = float(input('Ingrese los cm cubicos: '))
            if (cm < 0):
                print('Los cm no pueden ser negativos')
            else:
                return cm
        except:
            print('error')


def trans_cm_a_l(cm):
    litros = cm/1000
    print(f'{cm} cm3 = {litros} litros')


def pedir_li():
    while True:
        try:
            li = float(input('Ingrese los litros: '))
            if (li < 0):
                print('Los litros no pueden ser negativos')
            else:
                return li
        except:
            print('error')


def trans_l_a_cm(li):
    cm = li*1000
    print(f'{li} litros = {cm} cm3 ')


def pedir_pesos():
    while True:
        try:
            pesos = float(input('ingrese los pesos'))
            if (pesos < 0):
                print('Los pesos no son negativos')
            else:
                return pesos
        except:
            print('error')


def pesos_dolares(pesos):
    print(f'{pesos}AR = {round(pesos/280,0)}USD ')
