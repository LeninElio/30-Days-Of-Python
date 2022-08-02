# Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List,
# Tuple, Set and Dictionary.

# tipos de datos
# numeric
entero = 10
flotante = 10.2
complejo = 4 - 4j

# mas tipos
cadena = 'esta es una cadena'
boleano = True
lista = [1, 2, 3, 4, 5]
tupla = ('a', 'b', 'c', 'd')
conjunto = {'a', 'b', 'c', 'd', 1, 2, 3}
diccionario = {'nombre': 'lenin elio', 'edad': 25, 'pais': 'Peru'}

# Resultados
print(type(entero))
print(type(flotante))
print(type(complejo))
print(type(cadena))
print(type(boleano))
print(type(lista))
print(type(tupla))
print(type(conjunto))
print(type(diccionario))

# Find an Euclidian distance between (2, 3) and (10, 8)
# Longitud de un segmento. Distancia entre dos puntos. (2 dimensions)
p1 = 2
p2 = 3
q1 = 10
q2 = 8

Euclidian = (((q1 - p1) ** 2) + ((q2 - p2) ** 2)) ** (1 / 2)
print(f'La distancia mide {round(Euclidian, 2)}')
