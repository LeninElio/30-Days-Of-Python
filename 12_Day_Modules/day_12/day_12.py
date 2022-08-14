from funciones import *

# Escriba una función que genere un id_usuario_aleatorio de seis dígitos/caracteres.
print(random_user_id())

# Modificar la tarea anterior. Declare una función llamada user_id_gen_by_user. No toma ningún parámetro,
# pero toma dos entradas usando input(). Una de las entradas es la cantidad de caracteres y la segunda entrada es la
# cantidad de ID que se supone que se generarán.
# for i in user_id_gen_by_user():
#     print(i)

# Escribe una función llamada rgb_color_gen. Generará colores rgb (3 valores que van de 0 a 255 cada uno).
print(rgb_color_gen())

# Escriba una función list_of_hexa_colors que devuelva cualquier cantidad de colores hexadecimales en una matriz (
# seis números hexadecimales escritos después de #. El sistema de numeración hexadecimal está formado por 16
# símbolos, 0-9 y las primeras 6 letras del alfabeto, af. Verifique la tarea 6 para ejemplos de salida).
print(list_of_hexa_colors())

# Escriba una función list_of_rgb_colors que devuelva cualquier número de colores RGB en una matriz.
print(list_of_rgb_colors())

# Escriba una función generar_colores que pueda generar cualquier número de colores hexa o rgb.
print(generar_colores('hexa', 5))

# Llame a su función shuffle_list, toma una lista como parámetro y devuelve una lista mezclada
lista = ['a', 'b', 'c', 'd', 'e']
print(shuffle_list(lista))

# Escriba una función que devuelva una matriz de siete números aleatorios en un rango de 0-9. Todos los números deben
# ser únicos.
print(los_siete())

