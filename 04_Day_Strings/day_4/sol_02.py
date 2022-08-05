cadena = 'Codificación para todos'

# Solución 17
# Qué carácter está en el índice 10 en la cadena "Codificación para todos".
print(cadena[10])

# Solución 18
# Cree un acrónimo o una abreviatura para el nombre 'Python For Everyone'.
pfe = 'Python For Everyone'
cfa = 'Coding For All'
a, b, c = pfe.split()
print((a[0] + b[0] + c[0]).upper())

# Solución 19
# Cree un acrónimo o una abreviatura para el nombre 'Codificación para todos'.
a, b, c = cfa.split()
print((a[0] + b[0] + c[0]).upper())

# Solución 20
# Use index para determinar la posición de la primera aparición de C en Coding For All.
print(cfa.index('C'))

# Solución 21
# Utilice el índice para determinar la posición de la primera aparición de F en Coding For All.
print(cfa.find('F'))

# Solución 22
# Use rfind para determinar la posición de la última aparición de l en Coding For All People.
coding_for_people = 'Coding For All People'
print(coding_for_people.rfind('l'))

# Solución 23
# Use index o find para encontrar la posición de la primera aparición de la palabra 'porque' en la siguiente
# oración: 'No puede terminar una oración con porque porque porque es una conjunción'
texto_1 = 'No puede terminar una oración con porque porque porque es una conjunción'
print(texto_1.index('porque'))
print(texto_1.find('porque'))

# Solución 24
# Use rindex para encontrar la posición de la última aparición de la palabra porque en la siguiente oración:
# 'No puede terminar una oración con porque porque porque es una conjunción'
texto_2 = 'No puede terminar una oración con porque porque porque es una conjunción'
print(texto_2.rfind('porque'))
print(texto_2.rindex('porque'))


# Solución 25
# Corta la frase 'porque porque porque' en la siguiente oración: 'No puedes terminar una oración con porque
# porque porque es una conjunción'
texto_3 = 'No puedes terminar una oración con porque porque porque es una conjunción'
print(texto_3.replace(' porque porque porque ', ' '))

# Solución 26
# Encuentre la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 'No puede
# terminar una oración con porque porque porque es una conjunción'
print(texto_3.find('porque'))

# Solución 27
# Corta la frase 'porque porque porque' en la siguiente oración: 'No puedes terminar una oración con porque
# porque porque es una conjunción'
print(texto_3.split(' porque porque porque '))

# Solución 28
# ¿'Coding For All' comienza con una subcadena Coding?
subcadena = 'Coding'
print(cfa.startswith(subcadena))

# Solución 29
# ¿'Codificación para todos' termina con una codificación de subcadena?
print(cfa.endswith(subcadena))

# Solución 30
# ' Codificación para todos ', elimine los espacios finales izquierdo y derecho en la cadena dada.
codificar_para = ' Codificación para todos '
print(codificar_para)
print(codificar_para.strip(' '))