# Solucion 16 Encuentre la longitud del texto python y convierta el valor en flotante y conviértalo en una cadena
cadena = 'python'
valor = len(cadena)
valor = float(valor)

print(type(valor))
print(valor)

valor = str(valor)
print(type(valor))
print(valor)


# solucion 17 Los números pares son divisibles por 2 y el resto es cero. ¿Cómo verifica si un número es par o no
# usando python?

numero_par = int(input('Ingrese el numero para comprobar: '))
if numero_par % 2 == 0:
    print(f'{numero_par} es un numero par')
else:
    print(f'{numero_par} es un numero impar')

# Solucion 18 Verifique si la división del piso de 7 por 3 es igual al valor int convertido de 2.7.
floor_div = 7 // 3
value = 2.7

entero = int(value) == floor_div
print(entero)

# solucion 19 Compruebe si el tipo de '10' es igual al tipo de 10
diez_str = '10'
diez_num = 10

comprobar_diez = type(diez_str) == type(diez_num)
print(comprobar_diez)

# Solucion 20 Check if int('9.8') is equal to 10

gravedad = 9.81
comprobar_int = int(gravedad) == 10
print(comprobar_int)