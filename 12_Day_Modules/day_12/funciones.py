import random
import string as s


# Escriba una función que genere un id_usuario_aleatorio de seis dígitos/caracteres.
def random_user_id():
    num = s.digits
    letra = s.ascii_lowercase
    aleatorio = num + letra
    aleatorio = random.sample(aleatorio, 6)
    aleatorio = ''.join(aleatorio)
    return aleatorio


# Modificar la tarea anterior. Declare una función llamada user_id_gen_by_user. No toma ningún parámetro,
# pero toma dos entradas usando input(). Una de las entradas es la cantidad de caracteres y la segunda entrada es la
# cantidad de ID que se supone que se generarán.
def user_id_gen_by_user():
    lista = []
    ids = int(input("Ingrese la cantidad de ID's a generar: "))
    texto = int(input('Ingrese la cantidad de caracteres: '))

    num = s.digits
    letra = s.ascii_lowercase
    especial = s.punctuation
    aleatorio = num + letra + especial
    for i in range(1, ids + 1):
        aleatorio = random.sample(aleatorio, texto)
        aleatorio = ''.join(aleatorio)
        lista.append(aleatorio)
    return lista


# Escribe una función llamada rgb_color_gen. Generará colores rgb (3 valores que van de 0 a 255 cada uno).
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r}, {g}, {b})'


# Escriba una función list_of_hexa_colors que devuelva cualquier cantidad de colores hexadecimales en una matriz (
# seis números hexadecimales escritos después de #. El sistema de numeración hexadecimal está formado por 16
# símbolos, 0-9 y las primeras 6 letras del alfabeto, af. Verifique la tarea 6 para ejemplos de salida).

def list_of_hexa_colors():
    n = 6
    colors = []
    num = s.digits
    letra = s.ascii_uppercase
    letra = letra[:6]
    aleatorio = num + letra

    for i in range(1, n + 1):
        v1 = random.choice(aleatorio)
        v2 = random.choice(aleatorio)
        v3 = random.choice(aleatorio)
        v4 = random.choice(aleatorio)
        v5 = random.choice(aleatorio)
        v6 = random.choice(aleatorio)
        color = '#' + v1 + v2 + v3 + v4 + v5 + v6
        colors.append(color)
    return colors


# Escriba una función list_of_rgb_colors que devuelva cualquier número de colores RGB en una matriz.
def list_of_rgb_colors():
    n = 6
    colors = []
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    for i in range(1, n + 1):
        color = 'rgb(' + str(r) + ', ' + str(g) + ', ' + str(b) + ')'
        colors.append(color)
    return colors


# Escriba una función generar_colores que pueda generar cualquier número de colores hexa o rgb.
def generar_colores(tipo, cantidad):
    colors = []
    if tipo == 'hexa' or tipo == 'Hexa':
        num = s.digits
        letra = s.ascii_uppercase
        letra = letra[:6]
        aleatorio = num + letra
        for i in range(1, cantidad + 1):
            v1 = random.choice(aleatorio)
            v2 = random.choice(aleatorio)
            v3 = random.choice(aleatorio)
            v4 = random.choice(aleatorio)
            v5 = random.choice(aleatorio)
            v6 = random.choice(aleatorio)
            color = '#' + v1 + v2 + v3 + v4 + v5 + v6
            colors.append(color)
        return colors
    elif tipo == 'rgb' or tipo == 'RGB':
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        for i in range(1, cantidad + 1):
            color = 'rgb(' + str(r) + ', ' + str(g) + ', ' + str(b) + ')'
            colors.append(color)
        return colors
    else:
        return f'{tipo}, no puedo generar este color'


# Llame a su función shuffle_list, toma una lista como parámetro y devuelve una lista mezclada
def shuffle_list(lista):
    lista = ''.join(lista)
    shuffle = random.sample(lista, len(lista))
    return shuffle


# Escriba una función que devuelva una matriz de siete números aleatorios en un rango de 0-9. Todos los números deben
# ser únicos.
def los_siete():
    matriz = ()
    num = s.digits
    while len(matriz) < 7:
        val = random.choice(num)
        matriz = list(matriz)
        matriz.append(val)
        matriz = set(matriz)
    return matriz
