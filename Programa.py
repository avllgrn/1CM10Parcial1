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

# Se define la funcion
def gradosARadianes():
    # Se piden datos
    grados = float(input('Ingresa los grados '))

    # Se calcula la operación
    radianes = grados * math.pi / 180

    # Se muestra el resultado
    print(f'{grados}° = {radianes} rad')

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

# Menú de opciones que invoca a la función deseada por el usuario
print('1. Área y perímetro de un Círculo')
print('2. Conversión de grados a radianes')
print('3. Funciones Trigonométricas')
opcion = int(input('Qué opción quieres? ')) # Se pide la opción

# La función invocada está condicionada por la opción elegida por el usuario
if opcion == 1:
    areaYPerimetroDeCirculo()
else:
    if opcion == 2:
        gradosARadianes()
    else:
        if opcion == 3:
            funcionesTrigonometricas()
        else:
            print('Opcion invalida...')
