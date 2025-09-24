# Se define la funcion
def ifMenorDeEdad(edad):
    # Se calcula la operación y se retorna el resultado
    if edad < 18:
        return 'Eres menor de edad'
    else:
        return 'NO eres menor de edad'


# Se piden datos
edad = int(input('Ingresa tu edad '))

# Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
mensaje = ifMenorDeEdad(edad)

# Se muestra el resultado
print(f'{mensaje}')
