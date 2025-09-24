import math

# Se define la funcion
def areaDeCirculo(radio):
    # Se calcula la operación y se retorna el resultado
    return math.pi * radio**2

# Se define la funcion
def perimetroDeCirculo(radio):
    # Se calcula la operación y se retorna el resultado
    return 2 * math.pi *radio


# Se piden datos
radio = float(input('Ingresa el radio del círculo '))

# Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
area = areaDeCirculo(radio)
# Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
perimetro = perimetroDeCirculo(radio)

# Se muestra el resultado
print(f'radio = {radio}')
print(f'area = {area}')
print(f'perimetro = {perimetro}')
