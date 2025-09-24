# Se define la funcion
def ifEstadoCivil():
    estadoCivil = input('Ingresa tu estado civil (s/c/d/v) ')

    if estadoCivil == 's':
        print('Estado civil soltero')
    else:
        if estadoCivil == 'c':
            print('Estado civil casado')
        else:
            if estadoCivil == 'd':
                print('Estado civil divorciado')
            else:
                if estadoCivil == 'v':
                    print('Estado civil viudo')
                else:
                    print('Estado civil no es ni soltero, ni casado, ni divorciado, ni viudo')

# Se invoca la funcion
ifEstadoCivil()
