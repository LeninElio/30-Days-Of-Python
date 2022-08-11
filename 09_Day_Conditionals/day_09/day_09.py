# Ejercicios: Nivel 1
# Obtenga la entrada del usuario usando input ("Ingrese su edad:"). Si el usuario tiene 18 años o más, dé su opinión:
# tiene edad suficiente para conducir. Si es menor de 18, dé su opinión para esperar la cantidad de años que faltan.
# Producción:

edad = int(input('Ingrese su edad: '))

if edad > 18:
    print('Tiene edad suficiente para poder conducir')
else:
    print(f'Le faltan {18 - edad} anios para poder conducir')


