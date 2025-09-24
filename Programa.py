import math

# Se define la funcion
def radianesAGrados(grados):
    # Se calcula la operación y se retorna el resultado
    return radianes * 180 /  math.pi


# Se piden datos
radianes = float(input('Ingresa los radianes '))

# Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
grados = radianesAGrados(radianes)

# Se muestra el resultado
print(f'{radianes} rad = {grados}°')
