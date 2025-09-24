import math

# Se define la funcion
def formulaGeneralP(a, b, c):
    # Se calcula la operación y se retorna el resultado
    disc = math.pow(b,2) - 4*a*c
    if disc >= 0:
        if a != 0:
            return (-b+math.sqrt(disc)) / (2*a)
        else:
            return 'Raíces indeterminadas'
    else:
        return 'Raíces imaginarias'

# Se define la funcion
def formulaGeneralN(a, b, c):
    # Se calcula la operación y se retorna el resultado
    disc = math.pow(b,2) - 4*a*c
    if disc >= 0:
        if a != 0:
            return (-b-math.sqrt(disc)) / (2*a)
        else:
            return 'Raíces indeterminadas'
    else:
        return 'Raíces imaginarias'


# Se piden datos
a = float(input('Ingresa a '))
b = float(input('Ingresa b '))
c = float(input('Ingresa c '))

# Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
x1 = formulaGeneralP(a,b,c)

# Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
x2 = formulaGeneralN(a,b,c)

# Se muestra el resultado
print(f'a  = {a}')
print(f'b  = {b}')
print(f'c  = {c}')
print(f'x1 = {x1}')
print(f'x2 = {x2}')
