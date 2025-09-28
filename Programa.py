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
def gradosARadianes(grados):
    # Se calcula la operación y se retorna el resultado
    return grados * math.pi / 180

# Se define la funcion
def menu():
    # Menú de opciones que invoca a la función deseada por el usuario
    print('1. Área y perímetro de un Círculo')
    print('2. Conversión de grados a radianes')
    print('3. Funciones Trigonométricas')
    opcion = int(input('Qué opción quieres? ')) # Se pide la opción

    # La función invocada está condicionada por la opción elegida por el usuario
    if opcion == 1:
        areaYPerimetroDeCirculo()

    elif opcion == 2:
        # Se piden datos
        grados = float(input('Ingresa los grados '))

        # Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
        radianes = gradosARadianes(grados)

        # Se muestra el resultado
        print(f'{grados}° = {radianes} rad')

    else:
        print('Opcion invalida...')

# Se invoca la función del menú
menu()
