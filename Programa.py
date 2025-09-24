# Se define la funcion
def celciusAFahrenheit():
    # Se piden datos
    celcius = float(input('Ingresa los celcius '))

    # Se calcula la operación
    fahrenheit = 9/5*celcius + 32

    # Se muestra el resultado
    print(f'{celcius}°C = {fahrenheit}°F')

# Se invoca la funcion
celciusAFahrenheit()
