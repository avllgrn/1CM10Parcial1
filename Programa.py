import math

# Se define la funcion
def gradosARadianes():
    # Se piden datos
    grados = float(input('Ingresa los grados '))

    # Se calcula la operación
    radianes = grados * math.pi / 180

    # Se muestra el resultado
    print(f'{grados}° = {radianes} rad')

# Se invoca la funcion
gradosARadianes()
