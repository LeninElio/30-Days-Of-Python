# Use bucles anidados para crear lo siguiente:
n = 0
while n < 6:
    print('#' * 6)
    n += 1

# Imprime el siguiente patrón:
# for i in range(0, 10):
for j in range(0, 10):
    print(f'{j} x {j} = {j * j}')

# Iterar a través de la lista, ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] usando un bucle for e imprimir los
# elementos.
lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for n in lista:
    print(n)

# Use for loop para iterar de 0 a 100 e imprimir solo números pares
for i in range(0, 101, 2):
    print(i)

# Use for loop para iterar de 0 a 100 e imprimir solo números impares
for i in range(1, 101, 2):
    print(i)
