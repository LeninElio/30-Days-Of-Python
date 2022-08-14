# Declare una función llamada sum_of_odds. Toma un parámetro numérico y suma todos los números impares en ese rango.

def sum_of_odds(numero):
    suma = 0
    while numero > 0:
        if numero % 2 == 1:
            suma += numero
        numero -= 1
    return suma


print(sum_of_odds(5))


# Declare una función llamada sum_of_even. Toma un parámetro numérico y suma todos los números pares en ese rango.

def sum_of_even(numero):
    suma = 0
    while numero > 0:
        if numero % 2 == 0:
            suma += numero
        numero -= 1
    return suma


print(sum_of_even(5))


# Declare una función llamada evens_and_odds. Toma un entero positivo como parámetro y cuenta el número de pares e
# impares en el número.

def evens_and_odds(numero):
    impares = 0
    pares = 0
    while numero > 0:
        if numero % 2 == 1:
            impares += 1
        elif numero % 2 == 0:
            pares += 1
        numero -= 1
    return impares, pares


a, b = evens_and_odds(101)
print(f'La cantidad de numeros impares son {a}')
print(f'La cantidad de numeros pares son {b}')
