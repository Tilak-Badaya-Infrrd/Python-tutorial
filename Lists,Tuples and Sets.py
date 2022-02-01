courses = ['History' , 'Math' , 'Physics' , 'CompSci']

print(courses)
print(courses[1:3])
print(courses[-1])
courses.insert(0,'Art')
print(courses)

courses_2 = ['Humanities' , 'Arts']
courses.extend(courses_2)

print(courses)

popped = courses.pop()

print(popped)
print(courses)

courses.reverse()

print(courses)

courses.sort()

print(courses)
print(min(courses))
print(max(courses))
print(courses.index('Math'))
print('Math' in courses)

for item in courses:
    print(item)
    
for index,course in enumerate(courses):
    print(index,course)
    
course_str = ','.join(courses)

print(course_str)

new_list = course_str.split(',')

print(new_list)

tuple_1 = ('History' , 'Math' , 'Physics' , 'CompSci')

print(tuple_1)

tuple_2 = tuple_1

print(tuple_1==tuple_2)

courses_set = {'History' , 'Math' , 'Physics' , 'CompSci'}

print(courses_set)

empty_list = []
empty_tuple = ()
empty_set = set()