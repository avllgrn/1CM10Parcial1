import math

# Se define la funcion
def formulaGeneral():
    a = float(input('Ingresa a '))
    b = float(input('Ingresa b '))
    c = float(input('Ingresa c '))

    disc = math.pow(b,2) - 4*a*c
    if disc >= 0:
        if a != 0:
            x1 = (-b+math.sqrt(disc)) / (2*a)
            x2 = (-b-math.sqrt(disc)) / (2*a)
            print(f'a  = {a}')
            print(f'b  = {b}')
            print(f'c  = {c}')
            print(f'x1 = {x1}')
            print(f'x2 = {x2}')
        else:
            print('Raíces indeterminadas')
    else:
        print('Raíces imaginarias')

# Se invoca la funcion
formulaGeneral()
