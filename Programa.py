# Se define la funcion
def areaDeRectangulo(base,altura):
    # Se calcula la operación y se retorna el resultado
    return base*altura

# Se define la funcion
def perimetroDeRectangulo(base,altura):
    # Se calcula la operación y se retorna el resultado
    return 2*base + 2*altura


# Se piden datos
base = float(input('Ingresa la base del rectangulo '))
altura = float(input('Ingresa la altura del rectangulo '))

# Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
area = areaDeRectangulo(base,altura)
# Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
perimetro = perimetroDeRectangulo(base,altura)

# Se muestra el resultado
print(f'base = {base}')
print(f'altura = {altura}')
print(f'area = {area}')
print(f'perimetro = {perimetro}')
