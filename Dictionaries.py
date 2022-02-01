student = {'name':'John' , 'age' : 25 , 'courses' : ['Math' , 'CompSci']}

print(student['name'])
print(student.get('phone'))
print(student.get('phone','Not Found'))

student.update({'name':'Jane','phone':12345})

print(student)

age = student.pop('age')

print(student)
print(age)
print(len(student))
print(student.values())
print(student.items())

for key,values in student.items():
    print(key,values)