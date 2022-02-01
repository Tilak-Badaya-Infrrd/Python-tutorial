
import random
import datetime
import calendar
import os

courses = ['History' , 'Math' , 'Physics' , 'CompSci']
random_course = random.choice(courses)
today = datetime.date.today()

print(random_course)
print(today)
print(calendar.isleap(2020))
print(os.getcwd())
print(os.__file__)



