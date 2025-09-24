# Se define la funcion
def areaYPerimetroDeRectangulo():
    # Se piden datos
    base = float(input('Ingresa la base del rectangulo '))
    altura = float(input('Ingresa la altura del rectangulo '))

    # Se calcula la operación
    area = base*altura
    perimetro = 2*base + 2*altura

    # Se muestra el resultado
    print(f'base = {base}')
    print(f'altura = {altura}')
    print(f'area = {area}')
    print(f'perimetro = {perimetro}')


# Se invoca la funcion
areaYPerimetroDeRectangulo()
