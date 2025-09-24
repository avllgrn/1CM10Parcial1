# Se define la funcion
def fahrenheitACelcius(celcius):
    # Se calcula la operación y se retorna el resultado
    return (fahrenheit - 32) * 5/9


# Se piden datos
fahrenheit = float(input('Ingresa los fahrenheit '))

# Se invoca la funcion, se le envían argumentos, se recibe y se guarda resultado
celcius = fahrenheitACelcius(fahrenheit)

# Se muestra el resultado
print(f'{fahrenheit}°C = {celcius}°F')