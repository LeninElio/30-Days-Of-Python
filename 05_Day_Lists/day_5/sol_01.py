# Solución 01
# Declarar una lista vacía
lista = []

# Solución 02
# Declarar una lista con más de 5 elementos
lista_1 = [1, 2, 4, 5, 6, 7, 8, 5, 3, 21]

# Solución 03
# Encuentra la longitud de tu lista
print(len(lista_1))

# Solución 04
# Obtenga el primer elemento, el elemento del medio y el último elemento de la lista
print(lista_1[0])
medio = int(len(lista_1) / 2)
print(lista_1[medio])
print(lista_1[1])

# Solución 05
# Declare una lista llamada tipos_de_datos_mixtos, ponga su(nombre, edad, altura, estado civil, dirección)
tipos_de_datos_mixtos = ['Lenin elio', 26, 1.66, 'Soltero', 'Huaraz']

# Solución 06 Declare una variable de lista llamada it_companies y asigne valores iniciales Facebook, Google,
# Microsoft, Apple, IBM, Oracle y Amazon.
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Solución 07
# Imprime la lista usando print()
print(tipos_de_datos_mixtos)
print(companies)

# Solución 08
# Imprimir el número de empresas en la lista
print(f'La lista contiene la information de {len(companies)} empresas')

# Solución 09
# Imprimir la primera, segunda y última empresa
print(companies[0])
print(companies[1])
print(companies[-1])

# Solución 10
# Imprimir la lista después de modificar una de las empresas
print(companies)
companies[0] = 'Su pta madre Mark'
print(companies)

# Solución 11
# Agregar una empresa de TI a it_companies
print(companies)
companies.append('JetBrains')
print(companies)

# Solución 12
# Inserte una empresa de TI en medio de la lista de empresas
print(companies)
medio = int(len(companies)/2)
companies.insert(medio, 'PremiumSoft')
print(companies)

# Solución 13
# Cambie uno de los nombres de it_companies a mayúsculas (IBM excluido!)
companies[0] = companies[0].upper()
print(companies)

# Solución 14
# Únase a it_companies con una cadena '#;'
companies.append('#;  ')
print(companies)

# Solución 15
# Compruebe si una determinada empresa existe en la lista it_companies.
busca = 'Amazon' in companies
print(busca)