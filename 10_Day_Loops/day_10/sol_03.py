# Use for loop para iterar de 0 a 100 e imprimir la suma de todos los números.
suma = 0
for i in range(0, 101):
    suma += i
print(suma)

# Use for loop para iterar de 0 a 100 e imprimir la suma de todos los pares y la suma de todas las probabilidades.


par = 0
impar = 0
for i in range(0, 101):
    if i % 2 == 0:
        par += i
    else:
        impar += i

print(f'La suma de los numeros pares es {par} y la suma de los impares es {impar}')

# open('data/data.txt',)

with open("data/data.py", encoding='utf-8') as f:
    file = f.read()

# print(type(file))

print(country)
# for i in file:
#     print(i)
