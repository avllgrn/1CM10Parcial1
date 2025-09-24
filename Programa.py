import math

# Se define la funcion
def gradosARadianes(grados):
    # Se calcula la operación y se retorna el resultado
    return grados * math.pi / 180


# Se piden datos
grados = float(input('Ingresa los grados '))

# Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
radianes = gradosARadianes(grados)

# Se muestra el resultado
print(f'{grados}° = {radianes} rad')
