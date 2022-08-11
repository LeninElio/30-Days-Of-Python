# Aquí tenemos un diccionario de personas. ¡Siéntete libre de modificarlo!
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

"""
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node,
    Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, 
    Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions 
    can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
 
 Asabeneh Yetayeh lives in Finland. He is married.
"""
if person['skills']:
    print(person['skills'][len(person['skills']) // 2])
else:
    print('No skills')

if 'Python' in person['skills']:
    print('Python' in person['skills'], 'Se encuentra en la posicion: ', person['skills'].index('Python'))
else:
    print('No skills')

if 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('Es un desarrollador backend')
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('Él es un desarrollador fullstack')
elif 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print('Es un desarrollador front-end')
else:
    print('Título desconocido')
