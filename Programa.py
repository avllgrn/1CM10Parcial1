# Se define la funcion
def ifEstadoCivil(estadoCivil):
    # Se calcula la operación y se retorna el resultado
    if estadoCivil == 's':
        return 'Estado civil soltero'
    else:
        if estadoCivil == 'c':
            return 'Estado civil casado'
        else:
            if estadoCivil == 'd':
                return 'Estado civil divorciado'
            else:
                if estadoCivil == 'v':
                    return 'Estado civil viudo'
                else:
                    return 'Estado civil no es ni soltero, ni casado, ni divorciado, ni viudo'


# Se piden datos
estadoCivil = input('Ingresa tu estado civil (s/c/d/v) ')

# Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
mensaje = ifEstadoCivil(estadoCivil)

# Se muestra el resultado
print(f'{mensaje}')
