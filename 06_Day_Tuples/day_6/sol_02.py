# Ejercicios: Nivel 2
family_members = ('Rosa', 'Elisabeth', 'Elsa', 'Victoria', 'Vanessa', 'Marta', 'Juan', 'Pepe', 'Ramiro',
                  'Alberto', 'Patricio', 'Francisco', 'Padre', 'Madre')
print(family_members)

# Solución
# Desempaquetar hermanos y padres de family_members
hermanas = family_members[:5]
hermanos = family_members[6:11]
padres = family_members[12:]

print(hermanos)
print(hermanas)
print(padres)
# Solución Cree tuplas de frutas, verduras y productos animales. Une las tres tuplas y asígnalas a una variable
# llamada food_stuff_tp.
fruta = ('Manzana', 'Pera', 'Platano', 'Fresa', 'Pinia', 'Melon')
verdura = ('Tomate', 'Lechuga', 'Apio', 'Cebolla', 'Cilandro', 'Perejil')
p_animal = ('Pescado', 'Leche', 'Huevo', 'Mantequilla')

print(fruta)
print(verdura)
print(p_animal)

food_stuff_tp = fruta + verdura + p_animal
print(food_stuff_tp)

# Solución
# Cambie la tupla about food_stuff_tp a una lista food_stuff_lt
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Solución
# Rebane el artículo o artículos del medio de la tupla food_stuff_tp o la lista food_stuff_lt.
medio = len(food_stuff_lt)
print(medio)
if medio % 2 == 0:
    food_stuff_lt_1 = food_stuff_lt[:int(medio/2)]
    food_stuff_lt_2 = food_stuff_lt[int(medio/2):]
    print(food_stuff_lt_1)
    print(food_stuff_lt_2)
else:
    food_stuff_lt_1 = food_stuff_lt[int(medio/2):]
    print(food_stuff_lt_1)

# Solución
# Cortar los primeros tres elementos y los últimos tres elementos de la lista food_staff_lt
print(food_stuff_lt[(len(food_stuff_lt) - 3):])
print(food_stuff_lt[:3])

# Solución
# Eliminar completamente la tupla food_staff_tp
food_staff_tp = tuple(food_stuff_lt)
print(food_staff_tp)
del food_stuff_tp

# Solución
# Compruebe si existe un elemento en la tupla:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
search = 'Iceland' in nordic_countries
print(search)

