import math

# Se define la funcion
def funcionesTrigonometricas():
    # Se piden datos
    grados = float(input('Ingresa los grados '))

    # Se calcula la operación
    radianes = grados * math.pi / 180
    seno = math.sin(radianes)
    coseno = math.cos(radianes)
    tangente = math.tan(radianes)

    # Se muestra el resultado
    print(f'grados = {grados}')
    print(f'seno({grados})     = {seno}')
    print(f'coseno({grados})   = {coseno}')
    print(f'tangente({grados}) = {tangente}')

# Se invoca la funcion
funcionesTrigonometricas()