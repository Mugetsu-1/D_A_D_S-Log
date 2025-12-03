# Exception Handling => Error Handling

# num1 = 10
# num2 = 0
# print(num1/num2)

# list = [1,2,3,4,5]
# print(list[10])


# Error should be handled by using try and except block
# try => try block contains that type of code where an error may rise
# except => If the error rise in try block, the code to be executed is written inside except block 
# The except block is executed only if an error arise in try block
# IF the error didnot arise in try block, the code of try block is executed 

# finally => The finally block is executed anyway if the error arise or not

# num1 = 10
# num2 = 0
# list = [1,2,3]
# try:
#     print(num1/num2)
#     print(list[10])
# # except ZeroDivisionError as e:
# #     print(e)
# # except FileNotFoundError:
# #     print("FIle not found.")
# # except IndexError as e:
# #     print(e)
# except Exception as e:
#     print(e)
# finally:
#     print("Finally block executes anyway")

# try:
#     file = open("read.txt","r")
#     content = file.read()
#     file.close()
# except FileNotFoundError as e:
#     print(e)
#     file = open("read.txt","w")
#     file.close()


# Nested try except => try except vitra try except
# Nested if else => if else vitra if else
# Nested loop => loop vitra loop

try:
    pass
    try:
        try:
            pass
        except:
            pass
    except:
        try:
            pass
        except:
            pass
except:
    try:
        try:
            pass
        except:
            pass
    except:
        try:
            pass
        except:
            pass
        
# Update all the programs using try except
# Ecommerce task:
# add product, view product, update product, delete product
# Function, loop, file handling, exception handling 