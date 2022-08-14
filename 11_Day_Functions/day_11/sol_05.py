# Llame a su función factorial, toma un número entero como parámetro y devuelve un factorial del número
def factorial(numero):
    if numero == 1:
        return numero
    else:
        return numero * factorial(numero - 1)


print(factorial(5))


# Llame a su función is_empty , toma un parámetro y verifica si está vacío o no
def is_empty(valor=None):
    if valor is None:
        return 'Vacio'
    else:
        return f'Valor existente {valor}'


print(is_empty())

# Escribe diferentes funciones que toman listas. Deben calcular_media, calcular_mediana, calcular_modo,
# calcular_rango, calcular_varianza, calcular_std (desviación estándar).
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 5, 43, 2, 2, 3, 1, 2]
lista.sort()


# print(lista[0], lista[-1])

def calcular_media(numero):
    promedio = 0
    for i in numero:
        promedio += i
    return promedio / len(numero)


def calcular_mediana(numero):
    i = (len(numero) // 2) + 1
    if len(numero) % 2 == 0:
        promedio = (numero[i] + numero[i + 1]) / 2
        return promedio
    else:
        return numero[i]


def calcular_moda(numero):
    value = 0
    modas = []
    moda = []

    for i in numero:
        if i in modas:
            pass
        else:
            modas.append(i)

    for j in modas:
        if numero.count(j) > value:
            value = numero.count(j)
        else:
            value = value

    for x in modas:
        if numero.count(x) == value:
            moda.append(x)
        else:
            pass
    return moda


def calcular_rango(numero):
    mini = numero[0]
    maxi = numero[-1]
    return maxi - mini


def calcular_varianza(numero):
    suma = 0
    media = calcular_media(numero)
    for i in numero:
        suma += (i - media)**2
    return suma / len(numero)


def calcular_std(numero):
    var = calcular_varianza(numero)
    return var ** (1/2)


print('La media es: ', calcular_media(lista))
print('La mediana es: ', calcular_mediana(lista))
print('La moda es: ', calcular_moda(lista))
print('El rango es: ', calcular_rango(lista))
print('La varianza es: ', calcular_varianza(lista))
print('La desviación estándar es: ', calcular_std(lista))

