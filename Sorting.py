li = [9,4,5,2,7,1,8,0,6,3]

s_li = sorted(li)
print('Sorted Variable:\t', s_li)

print('Original Variable:\t', li)

li.sort()

print('Changed Variable:\t',li)

tup = (9,4,5,2,7,1,8,0,6,3)
s_tup = sorted(tup)
print('Tuple \t',s_tup)

di = {'name':'Corey' , 'job':'programming' , 'age':None , 'os': 'Linux'} 
s_di = sorted(di)
print('Dict\t',s_di)

li = [-6,-5,-4,1,2,3]
s_li = sorted(li)
print('Sorted Variable:\t', s_li)

s_li = sorted(li, key=abs)
print('Sorted Variable according to absolite values:\t', s_li)


