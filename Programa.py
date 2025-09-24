# Se define la funcion
def ifGenero():
    genero = input('Ingresa tu género (f/m) ')

    if genero == 'f':
        print('Genero femenino')
    else:
        if genero == 'm':
            print('Genero masculino')
        else:
            print('Genero no es ni femenino ni masculino')

# Se invoca la funcion
ifGenero()
