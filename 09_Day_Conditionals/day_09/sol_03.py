# Escriba un código que califique a los estudiantes de acuerdo con sus puntajes:
"""
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""

nota = float(input('Ingrese la nota del estudiante: '))

if 90 < nota <= 100:
    print(f'la nota del estudiante es {nota}, \npor ende la escala es A y el nivel de logro es "Logro destacado"')
elif 70 < nota <= 89:
    print(f'la nota del estudiante es {nota}, \npor ende la escala es B y el nivel de logro es "Logro esperado"')
elif 60 < nota <= 69:
    print(f'la nota del estudiante es {nota}, \npor ende la escala es C y el nivel de logro es "En proceso"')
elif 50 < nota <= 59:
    print(f'la nota del estudiante es {nota}, \npor ende la escala es D y el nivel de logro es "En inicio"')
elif 0 < nota <= 49:
    print(f'la nota del estudiante es {nota}, \npor ende la escala es E y el nivel de logro es "Sin logros"')