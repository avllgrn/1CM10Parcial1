import math

# Se define la funcion
def areaYPerimetroDeCirculo():
    # Se piden datos
    radio = float(input('Ingresa el radio del círculo '))

    # Se calcula la operación
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio

    # Se muestra el resultado
    print(f'radio = {radio}')
    print(f'area = {area}')
    print(f'perimetro = {perimetro}')

# Se invoca la funcion
areaYPerimetroDeCirculo()
