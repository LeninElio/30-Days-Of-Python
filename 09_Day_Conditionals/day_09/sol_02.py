# Compara los valores de my_age y your_age usando if... else. ¿Quién es mayor (tú o yo)? Use input ("Ingrese su
# edad:") para obtener la edad como entrada. Puede usar una condición anidada para imprimir 'año' para una diferencia
# de edad de 1 año, 'años' para diferencias mayores y un texto personalizado si mi_edad = su_edad. Producción:

mi_edad = 26
tu_edad = int(input('Ingrese su edad: '))

if tu_edad - mi_edad == 1:
    print(f'Eres {tu_edad - mi_edad} anio mayor que yo.')
elif tu_edad > mi_edad:
    print(f'Eres {tu_edad - mi_edad} anios mayor que yo.')
elif tu_edad == mi_edad:
    print('Tenemos la misma edad')
elif mi_edad - tu_edad == 1:
    print(f'Eres {mi_edad - tu_edad} anio menor que yo.')
else:
    print(f'Eres {mi_edad - tu_edad} anios menor que yo.')


# Obtenga dos números del usuario mediante el indicador de entrada. Si a es mayor que b, devuelve a es mayor que b,
# si a es menor, b devuelve a es menor que b, de lo contrario, a es igual a b. Producción:

na = int(input('Ingrese el primer numero: '))
nb = int(input('Ingrese el segundo numero: '))

if nb > na:
    print(f'{nb} es mayor que {na} por {nb - na}')
else:
    print(f'{nb} es menor que {na} por {na - nb}')