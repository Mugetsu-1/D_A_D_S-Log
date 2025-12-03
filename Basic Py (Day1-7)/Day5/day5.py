# Syntax: 
# while condition:
#       Code to be executed
# Most common mistake in while loop is it can generate infinite loop


# a = 10
# while a>0:
#     print(a)
#     a -= 1
     
     
# for i in range(10,0,-1):
#     print(i)


# Jaba samma user le exit vandaina tabasamma loop run grnu prney condition ma we use while loop 
# We have 2 differemt keywords used in loops : break and continue
# break : When break encouters, it completely exits the loop
# continue : When continue encounters, it skips the current iteration but keeps the loop running 

# break
# for i in range(10):
#     if i == 6:
#         break
#     print(i)
    
# for i in range(10):
#     if i == 6:
#         continue
#     print(i)




# while True:
#     choice = input("Emter 1 for addition, 2 for subtraction, 3 for exit: ")
#     if choice == '3':
#         break
#     num1 = int(input("ENter first number: "))
#     num2 = int(input("ENter second number: "))
#     match choice:
#         case '1':
#             print(num1+num2)
#         case '2':
#             print(num1-num2)
            
# Task: Update calulator task using while loop 

# We can use for loop in group data type using membership operator
# list1 = "saugat", "thapa"
# for i in list1:
#     print(i)

dict1 = {
    "name":"saugat",
    "surname":"Thapa",
    "age":29
}
for i in dict1:
    print(i)
    
# Task: Print all the values
