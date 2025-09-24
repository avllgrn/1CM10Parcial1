# Se define la funcion
def celciusAfahrenheit():
    # Se piden datos
    fahrenheit = float(input('Ingresa los fahrenheit '))

    # Se calcula la operación
    celcius = (fahrenheit - 32) * 5/9

    # Se muestra el resultado
    print(f'{fahrenheit}°C = {celcius}°F')

# Se invoca la funcion
celciusAfahrenheit()
