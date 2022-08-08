# Ejercicios: Nivel 3
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Solution
# Convierta las edades en un conjunto y compare la longitud de la lista y el conjunto, ¿cuál es más grande?
print(len(age))
sage = set(age)
print(sage)
print(len(sage))

# Solution
# Explique la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y conjunto
cadena = 'Esta es una cadena'
lista = [1, 2, 3, 3, 4, 5]
tupla = (1, 2, 3, 4, 5, 7, 8)
conjunto = {1, 2, 4, 6, 8, 9, 0}

# A una cadena se le puede asignar un solo valor
# Las listas son mutable y almacena elementos duplicados
# Las tuplas son inmutable (no se pueden modificar)
# Un conjunto es mutable, pero no almacena elementos duplicados

# Solution Soy profesora y me encanta inspirar y enseñar a la gente. ¿Cuántas palabras únicas se han usado en la
# oración? Use los métodos de división y configure para obtener las palabras únicas.
cadena = 'Soy profesora y me encanta inspirar y enseñar a la gente'
print(cadena)
lista = cadena.split(' ')
a = len(lista)
print(a)

conjunto = set(lista)
b = len(conjunto)
print(b)

print(f'las cantidad de palabras unicas usadas son: {a - (2*(a-b))}')