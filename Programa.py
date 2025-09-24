import math

# Se define la funcion
def senoDe(grados):
    # Se calcula la operación
    radianes = grados * math.pi / 180

    # Se calcula la operación y se retorna el resultado
    return math.sin(radianes)

# Se define la funcion
def cosenoDe(grados):
    # Se calcula la operación
    radianes = grados * math.pi / 180

    # Se calcula la operación y se retorna el resultado
    return math.cos(radianes)

# Se define la funcion
def TangenteDe(grados):
    # Se calcula la operación
    radianes = grados * math.pi / 180

    # Se calcula la operación y se retorna el resultado
    return math.tan(radianes)


# Se piden datos
grados = float(input('Ingresa los grados '))

# Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
seno = senoDe(grados)
# Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
coseno = cosenoDe(grados)
# Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
tangente = TangenteDe(grados)

# Se muestra el resultado
print(f'grados = {grados}')
print(f'seno({grados})     = {seno}')
print(f'coseno({grados})   = {coseno}')
print(f'tangente({grados}) = {tangente}')
