import keyword


# Escribe una función llamada is_prime, que verifica si un número es primo.
def is_prime(numero):
    contar = 0
    if numero > 1:
        for i in range(1, numero + 1):
            if numero % i == 0:
                contar += 1
            else:
                pass

        if contar > 2:
            return 'No es primo'
        else:
            return 'Es primo'
    else:
        return 'Ingrese un numero mayor que 1'


print(is_prime(1))

# Escriba una función que verifique si todos los elementos son únicos en la lista.
lista = [1, 2, 3, 4, 5, 'sds']


def verificar(numero):
    conjunto = set(numero)
    for i in conjunto:
        a = numero.count(i)
        if a > 1:
            return 'Hay elementos duplicados en la lista'
        else:
            return 'Elementos unicos en la lista'


print(verificar(lista))

# Escriba una función que compruebe si todos los elementos de la lista son del mismo tipo de datos.
tipos = []


def verificar_tipo(numero):
    for i in numero:
        tipos.append(type(i))

    for j in tipos:
        a = set(tipos)
        if len(a) > 1:
            return 'Hay diferentes tipos de datos en la lista'
        else:
            return 'La lista tiene los mismos tipos de datos'


print(verificar_tipo(lista))


# Escriba una función que verifique si la variable proporcionada es una variable de Python válida
numero = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def verificar_variable(variable):
    if variable.find(' ') > -1:
        return f'Nombre de variable no valida, no puede tener espacios'
    elif variable in keyword.kwlist:
        return f'Nombre de variable no valida, {variable} es una palabra reservada'
    elif variable[0] in numero:
        return f'Nombre de variable no valida, la variable no puede empezar por numero'
    else:
        return f'{variable} es un nombre valido'


print(verificar_variable('holamu ndo'))

