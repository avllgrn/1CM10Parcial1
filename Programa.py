# Se define la funcion
def areaYPerimetroDeCuadro():
    # Se piden datos
    lado = float(input('Ingresa el lado del cuadro '))

    # Se calcula la operación
    area = lado**2
    perimetro = 4*lado

    # Se muestra el resultado
    print(f'lado = {lado}')
    print(f'area = {area}')
    print(f'perimetro = {perimetro}')


# Se invoca la funcion
areaYPerimetroDeCuadro()
