genero = input('Ingresa tu género (f/m) ')
estadoCivil = input('Ingresa tu estado civil (s/c/d/v) ')

if genero == 'f':

    if estadoCivil == 's':
        print('Estado civil soltera')
    elif estadoCivil == 'c':
        print('Estado civil casada')
    elif estadoCivil == 'd':
        print('Estado civil divorciada')
    elif estadoCivil == 'v':
        print('Estado civil viuda')
    else:
        print('Género femenino, Estado civil no es ni soltero, ni casado, ni divorciado, ni viudo')

elif genero == 'm':
    if estadoCivil == 's':
        print('Estado civil soltero')
    elif estadoCivil == 'c':
        print('Estado civil casado')
    elif estadoCivil == 'd':
        print('Estado civil divorciado')
    elif estadoCivil == 'v':
        print('Estado civil viudo')
    else:
        print('Género masculino, Estado civil no es ni soltero, ni casado, ni divorciado, ni viudo')

else:
    if estadoCivil == 's':
        print('Genero no es ni femenino ni masculino, Estado civil soltero')
    elif estadoCivil == 'c':
        print('Genero no es ni femenino ni masculino, Estado civil casado')
    elif estadoCivil == 'd':
        print('Genero no es ni femenino ni masculino, Estado civil divorciado')
    elif estadoCivil == 'v':
        print('Genero no es ni femenino ni masculino, Estado civil viudo')
    else:
        print('Genero no es ni femenino ni masculino, Estado civil no es ni soltero, ni casado, ni divorciado, ni viudo')
