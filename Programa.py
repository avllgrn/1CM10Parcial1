# Se define la funcion
def sumaDeDosNumeros(primero, segundo):
    # Se calcula la operación y se retorna el resultado
    return primero + segundo


# Se piden datos
primero = float(input('Ingresa un número '))
segundo = float(input('Ingresa otro número '))

# Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
resultado = sumaDeDosNumeros(primero, segundo)

# Se muestra el resultado
print(f'{primero} + {segundo} = {resultado}')
