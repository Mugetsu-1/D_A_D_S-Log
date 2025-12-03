# Functions 
# A set of code that is ised to perform a paticular task
# Only by defining a function, the code wont run
# We need to call a function

# We till now did structural programming
# From now, we will be doing functional prgramming
# The benefit of functional programming : the code can be reused 

# def keyword is used to define a function

# Syntax:
# def function_name(parameter1, parameter2, parameter3 ...):
#       Code to be executed

# Calling a function
# function_name(arguments1, arguments2, arguments3 ...)

# There are 2 types of functions:
# 1. Built-in Functions : The functions that are alreay provided by Pyhton are built in functions.
# Eg: print(), input(), int(), str(), len(), lower()

# 2. User defined functions : The functions that are defined by the programmer according to their need

# def add():
#     a = 10
#     b = 20
#     print(a+b)

# add()
# print("hsadhjasdgas")
# add()
# print("sadjbsajsa")
# add()

# User defined functions are also of 2 types.
# Returnable function : The function that returns some value is called returnable function
# We use a return keyword to return a value
# Non Returnable Function : The function that does not return anything is non returnable function
# def add():
#     a = 10
#     b = 20
#     return a+b

# num = add()
# print(num)
# print("Ujjwal Neupane")
# print("hsadhjasdgas")
# num1 = add()
# print(num1)
# print("sadjbsajsa")
# num2 = add()
# print(num2)


# Arguments - Arguments are the values we send to the function during a function call
# Parameters - The variables in function that receives the arguments

# def add(a, b):
# print(a)
# print(b)
#     return a+b

# num = add(10,5)
# print(num)
# print("Ujjwal Neupane")
# print("hsadhjasdgas")
# num1 = add(20,30)
# print(num1)
# print("sadjbsajsa")
# num2 = add(15,25)
# print(num2)

# There are 2 types of arguments:
# 1. Positional Arguments - The parameters receives the arguments according to the position - args
# 2. Keyword Arguments - We send arguments in key value pair - kwargs
#  - The position doesnot matters in kwargs
# def add(a, b):
#     print(a)
#     print(b)
#     return a+b

# num = add(b=5,a=10)
# print(num)
# print("Ujjwal Neupane")
# print("hsadhjasdgas")
# num1 = add(20,30)
# print(num1)
# print("sadjbsajsa")
# num2 = add(15,25)
# print(num2)

# Args
# def abc(*args):
#     print(args)
    
# abc(1,2,3,4,5,"Ujjwal", "Neupane")

# # Kwargs
# def abc(**kwargs):
#     print(kwargs)
    
# abc(a=1,b=2,c=3,d=4,e=5,f="Ram", g="Hari")

# # Args and kwargs in a single function
# def abc(*args, **kwargs):
#     print("Args: ", args)
#     print("Kwargs: ", kwargs)
    
# abc("Neupane",5,8.5,a=10,b=25,name="Ujjwal")


# Types of Variables
# There are mainly 2 types of variables
# 1. Global Variable - The variable that is defined on the main program is called global variable.
#       Global variable is accessible from everywhere


# 2. Local Variable - The variable that is defined inside functions that cannot be accessible from everywhere
#       When the function ends, it ends the existence of the local variable

z = 5
def sum(a,b):
    print(z)
    print(a)
    print(a+b)
    
sum(10,5)
print(a)
print(z)
if True:
    print(z)
    
# Task: Update the calculator task using functions 