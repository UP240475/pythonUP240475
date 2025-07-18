#1-2
dog = {}

dog['name'] = 'Max'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5


#3-5
student = {
    'first_name': 'Diego',
    'last_name': 'Verdin',
    'gender': 'M',
    'age': 18,
    'marital_status': 'Soltero',
    'skills': ['Python', 'HTML'],
    'country': 'Mexico',
    'city': 'CDMX',
    'address': 'Calle xbox 123'
}

print(len(student))  

skills = student['skills']
print(skills)            
print(type(skills))      

#6-11
student['skills'].append('CSS')
student['skills'].append('JavaScript')
print(student['skills'])

keys = list(student.keys())
print(keys)

values = list(student.values())
print(values)

items = list(student.items())
print(items)

student.pop('marital_status')
print(student)

del dog