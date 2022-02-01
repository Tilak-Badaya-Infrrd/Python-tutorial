def hello_func():
    print("Hello Function")
    
hello_func()


def hello_func(greeting):
    return '{} Function.'.format(greeting)


print(hello_func('Hi'))


def hello_func(greeting,name='You'):
    return '{},{} Function.'.format(greeting,name)

print(hello_func('Hi'))
print(hello_func('Hi','Corey'))


def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
    
student_info('Math','Art',name='John',age=11)

courses = ['Math','Art']
info = {'name':'John','age':22}

student_info(*courses,**info)


