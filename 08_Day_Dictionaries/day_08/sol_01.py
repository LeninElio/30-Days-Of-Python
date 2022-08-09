# Solution
# Create an empty dictionary called dog
dog = {}
print(dog)

# Solution
# Add name, color, breed, legs, age to the dog dictionary
dog['color'] = 'Rojo'
dog['breed'] = 'Unknown'
dog['legs'] = 4
dog['age'] = 2
print(dog)

# Solution
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city
# and address as keys for the dictionary

student = {
    'first_name': 'Moreno Vega',
    'last_name': 'Lenin Elio',
    'gender': 'Male',
    'age': 26,
    'marital_status': 'S',
    'skills': ['Python', 'HTML', 'CSS', 'MySQL'],
    'country': 'Peru',
    'city': 'Huaraz',
    'address': {'Urbanization': 'Los Olivos', 'Number': 5, 'Ref': 'Primera curva'}
}

print(student)

# Solution
# Get the length of the student dictionary
print(len(student))

# Solution
# Get the value of skills and check the data type, it should be a list
a = student['skills']
print(a)
print(type(a))

# Solution
# Modify the skills values by adding one or two skills
student['skills'].append('SQLite')
student['skills'].append('SQL')
print(student)

# Solution
# Get the dictionary keys as a list
keys = student.keys()
print(keys)

# Solution
# Get the dictionary values as a list
values = student.values()
print(values)

# Solution
# Change the dictionary to a list of tuples using items() method
lista = student.items()
print(lista)

# Solution
# Delete one of the items in the dictionary
del student['city']
print(student)

# Solution
# Delete one of the dictionaries
del student
