# Solucion 06
ancho = float(input('Ingrese el ancho del reactangulo: '))
alto = float(input('Ingrese el alto del reactangulo: '))

area = ancho * alto
perimetro = 2 * (ancho + alto)

print(f'El area del reactangulo es {area}')
print(f'El perimetro del reactangulo es {perimetro}')

# Solucion 07 Obtenga el radio de un círculo usando el indicador. Calcula el área (área = pi x r x r) y la
# circunferencia (c = 2 x pi xr) donde pi = 3,14.

radio = float(input('Ingrese el radio de la circunferencia: '))

pi = 3.14

area = pi * radio ** 2
circunferencia = 2 * pi * radio

print(f'El area de la circunferencia es: {area}')
print(f'La circunferencia es: {circunferencia}')

# Solucion 08 Calcule la pendiente, la intersección x y la intersección y de y = 2x -2

# Solucion 09 La pendiente es (m = y2-y1/x2-x1). Encuentre la pendiente y la distancia euclidiana entre el punto (2,
# 2) y el punto (6,10)

x1, y1, x2, y2 = 2, 2, 6, 10

pendiente = (y2 - y1) / (x2 - x1)
distancia_euc = (((x2 - x1)**2) + ((y2 - y1)**2))**(1/2)

print(f'La pendiente de la recta es: {pendiente}')
print(f'La distancia euclideana es: {distancia_euc}')

# Solucion 10
# Compara las pendientes en las tareas 8 y 9.
