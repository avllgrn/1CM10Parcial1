# Se define la funcion
def celciusAFahrenheit(celcius):
    # Se calcula la operación y se retorna el resultado
    return 9/5*celcius + 32


# Se piden datos
celcius = float(input('Ingresa los celcius '))

# Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
fahrenheit = celciusAFahrenheit(celcius)

# Se muestra el resultado
print(f'{celcius}°C = {fahrenheit}°F')
