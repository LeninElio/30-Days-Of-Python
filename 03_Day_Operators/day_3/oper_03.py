# Solucion 11 Calcula el valor de y (y = x^2 + 6x + 9). Trate de usar diferentes valores de x y descubra en qué valor
# de x y será 0.

for x in range(-50, 50):
    y = x ** 2 + 6 * x + 9
    # print(f'cuando X vale: {x} Y vale: {y}')
    if y == 0:
        print(f'cuando X vale: {x}, Y vale: {y}')
        break
    else:
        pass

# Solucion 12 Encuentre la longitud de 'python' y 'dragon' y haga una declaración de comparación falsa.

python = 'Python'
dragon = 'Dragon'

comparar = len(python) is not len(dragon)
print(comparar)

# Solucion 13 Use un operador para verificar si 'on' se encuentra tanto en 'python' como en 'dragon'

verificar = 'on' in python and 'on' in dragon
print(verificar)

# Solucion 14 Espero que este curso no esté lleno de jerga . Use el operador in para verificar si hay jerga en la
# oración.

esperar = 'Espero que este curso no esté lleno de jerga'
buscar = 'jerga' in esperar
print(buscar)

# Solucion 15 No hay 'on' tanto en dragon como en python
verificar_on = 'on' not in python and 'on' not in dragon
print(verificar_on)