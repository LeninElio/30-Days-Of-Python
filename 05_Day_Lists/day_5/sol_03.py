from io import open

# Ejercicios: Nivel 2

# Solución 1
# La siguiente es una lista de las edades de 10 estudiantes:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Solución 1.1
# Ordena la lista y encuentra la edad mínima y máxima
ages.sort()
print(ages)
print(ages[0])
print(ages[-1])

# Solución 1.2
# Agregue la edad mínima y la edad máxima nuevamente a la lista
ages.append(28)
ages.append(17)
ages.sort()
print(ages)

# Solución 1.3
# Encuentre la edad mediana (un elemento intermedio o dos elementos intermedios divididos por dos)
if len(ages) % 2 == 0:
    middle = int(len(ages) / 2)
    print(ages[middle])
    print(ages[middle + 1])
else:
    middle = int(len(ages) / 2)
    print(ages[middle])

# Solución 1.4
# Encuentre la edad promedio (suma de todos los elementos dividida por su número)
suma = 0
for i in ages:
    suma += i
print(f'La edad promedio es {suma / len(ages)}')

print(sum(ages) / len(ages))
# Solución 1.5
# Encuentre el rango de las edades (max menos min)
rango = range(ages[0], ages[-1])
print(list(rango))
print(rango)

# Solución 1.6
# Compare el valor de () y (máx - promedio), use el método abs()
mini = ages[0] - (sum(ages) / len(ages))
maxi = ages[-1] - (sum(ages) / len(ages))

print(f'[mín - promedio] = {mini} \n[máx - promedio] = {maxi}')
print(f'[mín - promedio] = {abs(mini)} \n[máx - promedio] = {abs(maxi)}')

# Solución 2
# Encuentre el(los) país(es) intermedio(s) en la lista de países
archivo = open('country.txt', encoding='utf-8', mode='r')
texto = archivo.readlines()
archivo.close()
print(texto)
intermedio = int(len(texto) / 2)
print(texto[intermedio])

# Solución 3
# Dividir la lista de países en dos listas iguales si es aunque no sea un país más para la primera mitad.
intermedio_pais = int(len(texto) / 2)
pais_1 = texto[:intermedio_pais]
pais_2 = texto[intermedio_pais:]
print(f'En la lista 1 hay {len(pais_1)} paises')
print(pais_1)
print(f'En la lista 2 hay {len(pais_2)} paises')
print(pais_2)
print()

# Solución 4
# Descomprima los primeros tres países y el resto como países escandinavos.
country = ['China', 'Rusia', 'EE. UU.', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']
print(country)
pais_a, pais_b, pais_c, *escandinavos = country
print(pais_a)
print(pais_b)
print(pais_c)
print(escandinavos)
