# Consulta si la temporada es Otoño, Invierno, Primavera o Verano. Si la entrada del usuario es: septiembre,
# octubre o noviembre, la estación es otoño. Diciembre, enero o febrero, la temporada es invierno. Marzo,
# Abril o Mayo, la temporada es Primavera Junio, Julio o Agosto, la temporada es Verano

mes = str(input('Ingrese un mes del anio: '))

if mes == 'setiembre' or mes == 'octubre' or mes == 'noviembre':
    print('Esta en la estacion Otonio')
elif mes == 'diciembre' or mes == 'enero' or mes == 'febrero':
    print('Esta en la estacion Invierno')
elif mes == 'marzo' or mes == 'abril' or mes == 'mayo':
    print('Esta en la estacion Primavera')
elif mes == 'junio' or mes == 'julio' or mes == 'agosto':
    print('Esta en la estacion Verano')


# La siguiente lista contiene algunas frutas:
fruits = ['banana', 'orange', 'mango', 'lemon']
# Si una fruta no existe en la lista, agregue la fruta a la lista e imprima la lista modificada. Si la fruta existe
# print('Esa fruta ya existe en la lista')
fruta = str(input('Ingrese la fruta: '))

if fruta in fruits:
    print('Esa fruta ya existe en la lista')
else:
    fruits.append(fruta)
    print('Fruta agregada')
    print(fruits)