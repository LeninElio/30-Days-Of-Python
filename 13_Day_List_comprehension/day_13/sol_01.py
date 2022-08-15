# Filtre solo negativo y cero en la lista usando la comprensión de lista
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

lst = [i for i in numbers if i % 2 == 0 and i > 0]
print(lst)
print('-' * 25)
# Aplane la siguiente lista de listas de listas a una lista unidimensional:
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lst = [m for row in list_of_lists for i in row for m in i]
# mi_lista = [{operación con entrada n} for n in {python iterable}]

# for row in list_of_lists:
#     for j in row:
#         for x in j:
#             print(x)

print(lst)
print('-' * 25)
# Utilizando la comprensión de listas, cree la siguiente lista de tuplas:

lst = [(i, int((i / 1) - i), i, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(0, 11)]
print(lst)
print('-' * 25)
# Aplane la siguiente lista a una nueva lista:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lst = [[m[0], m[0][:4], m[1]] for i in countries for m in i]
# lst = [m for i in countries for m in i]
# [m[0], m[0][:4], m[1]]
# m.insert(1, m[0][:4])


print(lst)
print('-' * 25)

# List = [string[:3] for string in ('Geeks', 'for', 'Geeks')]

# for i in countries:
#     for j in i:
#         j = list(j)
#         j.insert(1, j[0][:4])
#         print(j)
#
# print('-' * 25)
# print(List)

# Cambie la siguiente lista de listas a una lista de cadenas concatenadas:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
lst = [m[0] + ' ' + m[1] for i in names for m in i]

print(lst)
print('-' * 25)


# Escriba una función lambda que pueda resolver una pendiente o una intersección con el eje y de funciones lineales.
# y = mx + b pendiente = m, intersection = b
