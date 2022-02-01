nums = [1,2,3,4,5,6,7,8,9,10]

my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

my_list = []
my_list = [n for n in nums]
print(my_list)

my_list = [n*n for n in nums]
print(my_list)

my_list = map(lambda n : n*n, nums)
print(my_list)

my_list = [n for n in nums if n%2==0]
print(my_list)

my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)


names = ['Bruce' , 'Clark' , 'Peter' , 'Wade']
heros = ['Batman' , 'Superman' , 'Spiderman' , 'Deadpool']

my_dict = {name:hero for name,hero in zip(names,heros)}
print(my_dict)

my_dict = {name:hero for name,hero in zip(names,heros) if name!='Peter'} 
print(my_dict)

my_set = set()

my_set = {n for n in nums}
print(my_set)


#Generator Expressions
#Yielding n*n for each 'n' in nums:

def gen_fun(nums):
    for n in nums:
        yield n*n
        
my_gen = gen_fun(nums)

for i in my_gen:
    print(i)
    
    
my_gen = (n*n for n in nums)
for i in my_gen:
    print(i)