# Declare una función suma_dos_números . Toma dos parámetros y devuelve una suma.
def suma(a, b):
    return a + b


print(suma(10, 13))


# El área de un círculo se calcula de la siguiente manera: área = π xrx r.
# Escribe una función que calcule area_of_circle .

def area_circle(radio):
    area = 3.14 * (radio ** 2)
    return area


print(area_circle(5))


# Escriba una función llamada add_all_nums que tome un número arbitrario de argumentos y los sume todos. Compruebe si
# todos los elementos de la lista son tipos de números. Si no, dé una respuesta razonable.

def suma_numero(*args):
    sumar = 0
    for i in args:
        sumar += i
    return sumar


a = suma_numero(12, 11, 34, 32, 23)
print(a)


# La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32.
# Escribe una función que convierta °C a °F, convert_celsius_to-fahrenheit.

def convert_c_f(temperatura):
    fahrenheit = (temperatura * (9 / 5)) + 32
    return fahrenheit


print(convert_c_f(43))


# Escribe una función llamada check-temporada, toma un parámetro de mes y devuelve la estación:
# Otoño, Invierno, Primavera o Verano.

def check_station(mes):
    if mes == 'enero' or mes == 'febrero' or mes == 'marzo':
        return 'primavera'
    elif mes == 'abril' or mes == 'mayo' or mes == 'junio':
        return 'verano'
    elif mes == 'julio' or mes == 'agosto' or mes == 'setiembre':
        return 'otonio'
    elif mes == 'octubre' or mes == 'noviembre' or mes == 'diciembre':
        return 'invierno'
    else:
        return 'El mes no existe'


print(check_station('mayo'))
