# Solución 01
# Concatene la cadena 'Treinta', 'Días', 'De', 'Python' en una sola cadena, 'Treinta días de Python'.
a, b, c, d, e = 'Treinta', 'Días', 'De', 'Python', ' '
concatenar = a + e + b + e + c + e + d
print(concatenar)

# Solución 02
# Concatene la cadena 'Codificación', 'Para', 'Todos' en una sola cadena, 'Codificación para todos'.
f, g, h = 'Codificación', 'Para', 'Todos'
concatena = '{} {} {}'.format(f, g, h)
print(concatena)

# Solución 03
# Declare una variable llamada empresa y asígnele un valor inicial "Codificación para todos".
empresa = "Codificación para todos"

# Solución 04
# Imprime la empresa variable usando print() .
print(empresa)

# Solución 05
# Imprima la longitud de la cadena de caracteres de la empresa utilizando el método len() e print() .
print(len(empresa))

# Solución 06
# Cambie todos los caracteres a letras mayúsculas usando el método upper().
print(empresa.upper())

# Solución 07
# Cambie todos los caracteres a letras minúsculas usando el método lower().
print(empresa.lower())

# Solución 08
# Use los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena Coding For All.
print(empresa.capitalize())
print(empresa.title())
print(empresa.swapcase())

# Solución 09
# Corte (corte) la primera palabra de la cadena Coding For All.
corte = empresa.strip('Codificación')
print(corte)

# Solución 10
# Verifique si la cadena Coding For All contiene una palabra Coding utilizando el método index, find u otros métodos.
print(empresa)
busca = 'Codificación'
print(empresa.index(busca))
print(empresa.find(busca))

# Solución 11
# Reemplace la palabra codificación en la cadena 'Codificación para todos' por Python.
print(empresa.replace(busca, 'Python'))

# Solución 12
# Cambie Python para todos a Python para todos usando el método de reemplazo u otros métodos.
cadena_1 = 'Python for Everyone'
cadena_2 = 'Python for All'
print(cadena_1)
print(cadena_1.replace('Everyone', 'All'))

cadena_x = cadena_1[:10]
print(cadena_x + ' All')

# Solución 13
# Divida la cadena 'Codificación para todos' usando el espacio como separador (split()).
print(empresa.split(' '))

# Solución 14
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" divide la cadena en la coma.
datos_entrada = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(datos_entrada.split(', '))

# Solución 15
# ¿Cuál es el carácter en el índice 0 en la cadena Coding For All?
print(empresa[0])

# Solución 16
# ¿Cuál es el último índice de la cadena Coding For All?
print(empresa[-1])
