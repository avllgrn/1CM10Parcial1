# Se define la funcion
def ifGeneroEstadoCivil():
    genero = input('Ingresa tu género (f/m) ')
    estadoCivil = input('Ingresa tu estado civil (s/c/d/v) ')

    if genero == 'f':
        if estadoCivil == 's':
            print('Estado civil soltera')
        else:
            if estadoCivil == 'c':
                print('Estado civil casada')
            else:
                if estadoCivil == 'd':
                    print('Estado civil divorciada')
                else:
                    if estadoCivil == 'v':
                        print('Estado civil viuda')
                    else:
                        print('Género femenino, Estado civil no es ni soltero, ni casado, ni divorciado, ni viudo')
    else:
        if genero == 'm':
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
                            print('Género masculino, Estado civil no es ni soltero, ni casado, ni divorciado, ni viudo')
        else:
            if estadoCivil == 's':
                print('Genero no es ni femenino ni masculino, Estado civil soltero')
            else:
                if estadoCivil == 'c':
                    print('Genero no es ni femenino ni masculino, Estado civil casado')
                else:
                    if estadoCivil == 'd':
                        print('Genero no es ni femenino ni masculino, Estado civil divorciado')
                    else:
                        if estadoCivil == 'v':
                            print('Genero no es ni femenino ni masculino, Estado civil viudo')
                        else:
                            print('Genero no es ni femenino ni masculino, Estado civil no es ni soltero, ni casado, ni divorciado, ni viudo')


# Se invoca la funcion
ifGeneroEstadoCivil()
