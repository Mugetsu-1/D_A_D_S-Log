# names = "Ujjwal ABC DEF GHI Neupane"
# listnames = names.split() # split converts string to list
# print(listnames)
# print(type(listnames))


# list = [1,2,4,"Ujjwal","Neupane",[1,2,3]]
# print(type(list))


# Tuple - Same like list but it is wrapped with ( ). Tuple is non mutable data type.
# tuple = (1,2,3,4,5)
# print(type(tuple))

# # Sets - Wrapped with { } and has no fixed index
# set1 = {1,"ABC",2,"Ujjwal","Neupane"}
# print(type(set1))
# print(set1)


# Dictionary - Always appears in key-value pair and is wrapped with { }

# dict1 = {
#     "name":"Ujjwal",
#     "age":29,
#     "position":"Data Scientist"
# }
# print(type(dict1))


# Indexing and Slicing
# Indexing - Accessing a particular element from a group data type
# Slicing - Accessing the list of elements from a group data type

# list1 = [1,2,3,4,5,6,7,8,9]
# print(list1[5])
# print(list1[8])

# print(list1[4:8])
# print(list1[:5])
# print(list1[5:])

# Task: Implement indexing and slicing as same type in other data types also
# Tuple, String

# TODO:

# Create a list of usernames
# Input a username from the user
# Check if the username is present in the list or not

# 2. Create a dictionary of usernames and passwords, 
# 	extract all the usernames from the dictionary and 	input username from the user and check if the 	username is present in the extracted list of 	usernames



# Conditional Statements
# Statements executes according to condition
# if and else keyword is used in if else
# Syntax:
# if condition:
#       Code to be executed if conditin == True
# else:
#       Code to be executed if condition == False

# a = 5
# b = 8
# if a > b:
#     print(a)
# else:
#     print(b)
    
# list = ["Saugat","Thapa",5,8,10,"ABC","Ram"]
# if "Ram" in list:
#     print("Ram is found in list")
# else:
#     print("Ram is not found in the list.")

dict = {
    "name":"Saugat",
    "surname":"Thapa"
}

# if "saugat" in dict:
#     print("name found")
# else:
#     print("name not found")

# Elif ladder

marks = 65

if marks >=90:
    print("A+")
elif marks >=80 and marks<90:
    print("A")
elif marks >=70 and marks<80:
    print("B+")
elif marks>=60 and marks < 70:
    print("B")
else:
    print("Fail")