# Ejercicios: Nivel 2

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Solution 01
# Une A y B
unido = A.union(B)
print(unido)

# Solution 02
# Encuentra una intersección B
inter = A.intersection(B)
print(inter)

# Solution 03
# es un subconjunto de B
print(B.issubset(A))
print(A.issubset(B))

# Solution 04
# ¿Son A y B conjuntos disjuntos?
print(A.isdisjoint(B))

# Solution 05
# Unir A con B y B con A
ab = A.union(B)
ba = B.union(A)
print(ab)
print(ba)

# Solution 06
# ¿Cuál es la diferencia simétrica entre A y B?
print(A.symmetric_difference(B))

# Solution 07
# Eliminar los conjuntos por completo
del A
del B
