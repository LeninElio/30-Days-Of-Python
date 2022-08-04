# Solucion 21 Escriba un script que solicite al usuario que ingrese las horas y la tarifa por hora. ¿Calcular el
# salario de la persona?

hora = float(input('Ingrese las horas trabajadas: '))
tarifa = float(input('Ingrese la tarifa por hora trabajada: '))

salario = hora * tarifa
print(salario)

# Solucion 22 Escriba un script que solicite al usuario que ingrese el número de años. Calcular el número de segundos
# que puede vivir una persona. Supongamos que una persona puede vivir cien años.

anio = int(input('Ingrese el numero de a;os que tiene: '))

segundos = anio * 365 * 24 * 60 * 60
print(f'Usted ha vivido {segundos} segundos')

# solucion 23
# Escriba un script de Python que muestre la siguiente tabla
tabla = '''1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125'''

print(tabla)