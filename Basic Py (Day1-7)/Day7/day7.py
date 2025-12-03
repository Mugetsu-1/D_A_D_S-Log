# Typs of functions:

# lambda functions: The function that is written in a single line
# lambda keyword is used to define a lambda function 

add = lambda x,y,z : print(x + y)
add(4,5,6)



numbers = [x for x in range(1,10,2)]
print(list(map(lambda a : a+5, numbers)))

numbers = [x for x in range(1,10,2)]
print(list(filter(lambda x : x*2<10, numbers)))

from functools import reduce
numbers = [x for x in range(1,6)] # [ 1,2,3,4,5]
print(reduce(lambda x,y : x*y, numbers))

list1 = [x for x in range(15)]
list2 = [x for x in range(2,13)]
list3 = [x for x in range(5,13)]

print(list(zip(list1,list2, list3)))