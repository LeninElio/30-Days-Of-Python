# Escriba una función llamada calcular_pendiente que devuelva la pendiente de una ecuación lineal

# (x1, y1)
# (x2, y2)

def pendiente(x1, x2, y1, y2):
    calculo = (y2 - y1) / (x2 - x1)
    return calculo


print(pendiente(2, 4, 1, 7))


# La ecuación cuadrática se calcula de la siguiente manera: ax² + bx + c = 0. Escriba una función que calcule el
# conjunto de soluciones de una ecuación cuadrática, solve_quadratic_eqn .

def solve_quadratic_eqn(a, b, c):
    if a == 0:
        print('a No puede tomar el valor 0')
    else:
        valor_1 = (-b + ((b ** 2) - (4 * a * c)) ** (1 / 2)) / (2 * a)
        valor_2 = (-b - ((b ** 2) - (4 * a * c)) ** (1 / 2)) / (2 * a)
        return valor_1, valor_2


print(solve_quadratic_eqn(2, 9, 10))

# Declare una función llamada print_list. Toma una lista como parámetro e imprime cada elemento de la lista.
argumentos = []


def print_list(*args):
    for i in args:
        argumentos.append(i)
    return argumentos


print(print_list('a', 'b', 'c'))


# Declare una función llamada lista_inversa. Toma una matriz como parámetro y devuelve el reverso de la matriz
# (uso de bucles).
n = []


def lista_inversa(lista):
    for i in lista:
        x = (len(lista) - i)
        n.append(lista[x])
    return n


print(lista_inversa([1, 2, 3, 4, 5]))
