if True:
    print('Conditional was True')
    
language = 'Python'

if language=='Python':
    print('Conditional was True')
    
language = 'Java'

if language == 'Python':
    print('language is Python')
elif language == 'Java':
    print('language is Java')
else:
    print("Neither")
    
print(0 and 1)
print(False or True)
print(True and False)


user = 'Admin'
logged_in = False

if user=='Admin' and logged_in:
    print("Admin logged in")
else:
    print("Please log in")
    
user = 'Admin'
logged_in = False

if user=='Admin' or logged_in:
    print("Admin logged in")
else:
    print("Please log in")
    
    
a = [1,2,3]
b = a

print(a==b)
print(id(a)==id(b))
