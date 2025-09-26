estadoCivil = input('Ingresa tu estado civil (s/c/d/v) ')

if estadoCivil == 's':
    print('Estado civil soltero')
elif estadoCivil == 'c':
    print('Estado civil casado')
elif estadoCivil == 'd':
    print('Estado civil divorciado')
elif estadoCivil == 'v':
    print('Estado civil viudo')
else:
    print('Estado civil no es ni soltero, ni casado, ni divorciado, ni viudo')
