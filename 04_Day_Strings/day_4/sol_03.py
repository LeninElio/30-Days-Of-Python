# Solución
# ¿Cuál de las siguientes variables devuelve True cuando usamos el método isidentifier():
texto_1 = '30DíasDePython'
texto_2 = 'treinta_dias_de_python'
print(texto_1.isidentifier())
print(texto_2.isidentifier())

# Solución
# La siguiente lista contiene los nombres de algunas de las bibliotecas de Python:
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Únase a la lista con un hash con cadena de espacio.
biblioteca = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
resultado = '# '.join(biblioteca)
print(resultado)

# Solución
# Use la secuencia de escape de nueva línea para separar las siguientes oraciones.
oration_1 = 'I am enjoying this challenge.'
oration_2 = 'I just wonder what is next.'
resulta = f'{oration_1} \n{oration_2}'
print(resulta)

# Solución
# Use una secuencia de escape de tabulación para escribir las siguientes líneas.
datos_1 = ['Name', 'Age', 'Country', 'City', 'Asabeneh', 250, 'Finland', 'Helsinki']
print(f'{datos_1[0]} \t{datos_1[1]} \t{datos_1[2]} \t{datos_1[3]} \n{datos_1[4]} \t{datos_1[5]} \t{datos_1[6]} \t{datos_1[7]}')

# Solución
# Utilice el método de formato de cadena para mostrar lo siguiente:
radius = 10
area = 3.14 * radius ** 2
resultar = 'The area of a circle with radius {} is {} meters square.'.format(radius, area)
print(resultar)

# Solución
# Haga lo siguiente usando métodos de formato de cadena:
a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
