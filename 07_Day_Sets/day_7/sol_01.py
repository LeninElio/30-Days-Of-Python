# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Ejercicios: Nivel 1

# Solucion 01
# Encuentre la longitud del conjunto it_companies
print(len(it_companies))

# Solucion 02
# Agregar 'Twitter' a it_companies
it_companies.update(['Twitter'])
print(it_companies)

# Solucion 03
# Inserte varias empresas de TI a la vez en el conjunto it_companies
add_list = ['Jetbrains', 'Indra', 'Cassandra', 'Anaconda']
it_companies.update(add_list)
it_companies.union(add_list)
print(it_companies)

# Solucion 04
# Eliminar una de las empresas del conjunto it_companies
it_companies.remove('Facebook')
print(it_companies)

# Solucion 05
# ¿Cuál es la diferencia entre eliminar y descartar?
it_companies.discard('Facebook')
print(it_companies)
# Cuando no encuentra el elemento, update devuelve un error, discard no
