import math

# Se define la funcion
def radianesAGrados():
    # Se piden datos
    radianes = float(input('Ingresa los radianes '))

    # Se calcula la operación
    grados = radianes * 180 /  math.pi

    # Se muestra el resultado
    print(f'{radianes} rad = {grados}°')

# Se invoca la funcion
radianesAGrados()
