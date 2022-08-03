# Dia 02, 30 dias de programacion en python

# Ejercicios de nivel 1
import math

nombre = 'Lenin Elio'
apellido = 'Moreno Vega'
nombre_completo = 'Lenin Elio Moreno Vega'
pais = 'Peru'
ciudad = 'Huaraz'
edad = 26
anio = '2022'
es_casado = False
es_verdadero = True
luz_encendida = True

correo, direccion, lenguaje = 'morenolenienlio@gmail.com', 'Huaraz, Ancash', 'Python'

# Ejercicios de nivel 2
# 2.1
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(anio))
print(type(es_casado))
print(type(es_verdadero))
print(type(luz_encendida))
print(type(correo))
print(type(direccion))
print(type(lenguaje))

# 2.2
print(len(nombre))

# 2.3
print(f'Tamanio del apellido {len(apellido)}, tamanio del nombre {len(nombre)}')

# 2.4
num_one = 5
num_two = 4

suma = num_two + num_one
print(suma)

resta = num_two - num_one
print(resta)

multiplicar = num_two * num_one
print(multiplicar)

dividir = num_one / num_two
print(dividir)

potencia = num_one**num_two
print(potencia)

modulo = num_one % num_two
print(modulo)

# 2.5
radio = 30

# Area del circulo
area_of_circle = math.pi * (radio ** 2)
print('El area del circulo es: ', area_of_circle)

# Circunferencia del circulo
circum_of_circle = math.pi * (2 * radio)
print('La circunferencia del circulo es: ', circum_of_circle)

radio_entrada = int(input('Ingrese la radio de la circunferencia: '))
area_circulo = math.pi * (radio_entrada ** 2)
print('El area del circulo es: ', area_circulo)

# 2.6

nombre = str(input('Como te llamas?: '))
apellido = str(input('Cual es tu apellido?: '))
pais = str(input('De que pais eres?: '))
edad = str(input('Que edad tienes?: '))

print(nombre, apellido, pais, edad)

# 2.7
print('help("keywords")')




















