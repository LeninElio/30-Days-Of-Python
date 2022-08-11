# Itere de 0 a 10 usando el bucle for, haga lo mismo usando el bucle while.
for i in range(0, 10):
    print(i)
print('-' * 25)

n = 0
while n < 10:
    print(n)
    n += 1
print('-' * 25)
# Itere de 10 a 0 usando el bucle for, haga lo mismo usando el bucle while.
m = 10
while m >= 1:
    print(m)
    m -= 1
print('-' * 25)

num = 10
for s in range(1, num):
    print(num - s)
print('-' * 25)
# Escriba un bucle que haga siete llamadas a print(), de modo que obtengamos en la salida el siguiente triángulo:
for i in range(1, 8):
    print('#' * i)
