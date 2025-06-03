#saber si un número es par o impar

numero= int(input('Ingrese un año cualquiera: '))

if numero % 4 == 0:
    if numero > 2025:
        print(f' El año: {numero} será bisiesto')
    else:
        print(f'El año {numero} fue bisiesto')
else:
    if numero > 2025:
        print(f' El año: {numero} no será bisiesto')

    else:
        print(f'El año {numero} no fue bisiesto')