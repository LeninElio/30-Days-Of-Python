# Ejercicios: Nivel 1

# Solucion 1
# Crear una tupla vacía
tup_1 = ()
print(tup_1)

# Solucion 2
# Crea una tupla que contenga los nombres de tus hermanas y tus hermanos (los hermanos imaginarios están bien)
hermanos = ('Juan', 'Pepe', 'Ramiro', 'Alberto', 'Patricio', 'Francisco')
print(hermanos)

# Solucion 3
# Unir tuplas de hermanos y hermanas y asignarlas a hermanos
hermanas = ('Rosa', 'Elisabeth', 'Elsa', 'Victoria', 'Vanessa', 'Marta')
union = hermanas + hermanos
print(hermanas)
print(union)

# Solucion 4
# ¿Cuántos hermanos tiene usted?
print(len(hermanos))

# Solucion 5
# Modifique la tupla de hermanos y agregue el nombre de su padre y madre y asígnelo a family_members
family_members = list(union)
print(family_members)

family_members.append('Padre')
family_members.append('Madre')
print(family_members)

family_members = tuple(family_members)
print(family_members)