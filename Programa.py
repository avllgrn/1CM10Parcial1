edad = int(input('Ingresa tu edad '))

if edad < 0:
    print('Error! Edad invalida (-)')
elif edad < 18:
    print('Eres menor de edad')
elif edad < 100:
    print('Eres mayor de edad')
else:
    print('Error! Edad invalida (+)')
