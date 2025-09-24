# Se define la funcion
def ifGenero(genero):
    # Se calcula la operación y se retorna el resultado
    if genero == 'f':
        return 'Genero femenino'
    else:
        if genero == 'm':
            return 'Genero masculino'
        else:
            return 'Genero no es ni femenino ni masculino'


# Se piden datos
genero = input('Ingresa tu género ')

# Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
mensaje = ifGenero(genero)

# Se muestra el resultado
print(f'{mensaje}')
