radius = 10
pi = 3.14
area = pi * radius ** 2
format_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area)

"""
Sintaxis: {[argument_index_or_keyword]:[width][.precision][type]}

Se type puede utilizar con códigos de formato:

Códigos de formato	Descripción
d	para enteros
f	para números de coma flotante
b	para números binarios
o	para números octales
x	para números octales hexadecimales
s	para strings
e	para punto flotante en formato de exponente
"""

cadena = 'Python para todos'
numero = 3.112342325

pruebas = 'Hola mundo este es un {:.6s}'.format(cadena)
print(pruebas)

print(f'Datos que no tengo ni idea {2}, {1}, {0}'.format(*'abc'))

datos = {'nombre': 'Lenin Elio', 'apellido': 'Moreno Vega'}
print('Datos de la persona: {nombre}, {apellido}'.format(**datos))
