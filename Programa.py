# Se define la funcion
def areaDeCuadro(lado):
    # Se calcula la operación y se retorna el resultado
    return lado**2

# Se define la funcion
def perimetroDeCuadro(lado):
    # Se calcula la operación y se retorna el resultado
    return 4*lado


# Se piden datos
lado = float(input('Ingresa el lado del cuadro '))

# Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
area = areaDeCuadro(lado)
# Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
perimetro = perimetroDeCuadro(lado)

# Se muestra el resultado
print(f'lado = {lado}')
print(f'area = {area}')
print(f'perimetro = {perimetro}')
